document.addEventListener('DOMContentLoaded', () => {
    // Initialize Chart
    const ctx = document.getElementById('mainChart').getContext('2d');
    
    // Gradient for the chart line
    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgba(59, 130, 246, 0.5)');
    gradient.addColorStop(1, 'rgba(59, 130, 246, 0.0)');

    let myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            datasets: [{
                label: 'Simulated Price Trend',
                data: [150, 155, 148, 160, 165, 158, 170],
                borderColor: '#3b82f6',
                backgroundColor: gradient,
                borderWidth: 2,
                pointBackgroundColor: '#1e293b',
                pointBorderColor: '#3b82f6',
                pointBorderWidth: 2,
                pointRadius: 4,
                pointHoverRadius: 6,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.9)',
                    titleColor: '#f8fafc',
                    bodyColor: '#94a3b8',
                    borderColor: '#334155',
                    borderWidth: 1,
                    padding: 12,
                    displayColors: false,
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(51, 65, 85, 0.5)', drawBorder: false },
                    ticks: { color: '#94a3b8' }
                },
                y: {
                    grid: { color: 'rgba(51, 65, 85, 0.5)', drawBorder: false },
                    ticks: { color: '#94a3b8' }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index',
            },
        }
    });

    // Elements
    const searchBtn = document.getElementById('search-btn');
    const tickerInput = document.getElementById('ticker-input');
    
    const predValue = document.getElementById('pred-value');
    const confValue = document.getElementById('conf-value');
    const sentValue = document.getElementById('sent-value');
    const mentionsValue = document.getElementById('mentions-value');
    const currentTickerHeader = document.getElementById('current-ticker');

    // Fetch API logic
    searchBtn.addEventListener('click', async () => {
        const ticker = tickerInput.value.trim().toUpperCase();
        if(!ticker) return;

        // Visual loading state
        predValue.textContent = '...';
        confValue.textContent = '...';
        sentValue.textContent = '...';
        mentionsValue.textContent = '...';
        searchBtn.textContent = 'Loading...';

        try {
            const response = await fetch(`/api/predict?ticker=${ticker}`);
            const data = await response.json();

            // Update UI
            currentTickerHeader.textContent = `${data.ticker} Overview`;
            
            // Prediction Color
            predValue.textContent = data.prediction;
            predValue.className = 'metric-value'; // reset classes
            if(data.prediction === 'BULLISH') {
                predValue.classList.add('indicator-bullish');
            } else {
                predValue.classList.add('indicator-bearish');
            }

            confValue.textContent = `${(data.confidence * 100).toFixed(0)}%`;
            sentValue.textContent = data.sentiment_score.toFixed(2);
            mentionsValue.textContent = data.recent_mentions;

            // Update chart with real historical data if available
            if (data.historical_dates && data.historical_prices && data.historical_dates.length > 0) {
                myChart.data.labels = data.historical_dates;
                myChart.data.datasets[0].data = data.historical_prices;
                myChart.data.datasets[0].label = `${ticker} Price Trend`;
                myChart.update();
            } else {
                // Fallback to random data if ticker has no real stock price history
                const newData = Array.from({length: 7}, () => Math.floor(Math.random() * 50) + 100);
                myChart.data.datasets[0].data = newData;
                myChart.data.datasets[0].label = `${ticker} Price Trend (No real data)`;
                myChart.update();
            }

        } catch (error) {
            console.error('Error fetching prediction:', error);
            predValue.textContent = 'ERROR';
        } finally {
            searchBtn.textContent = 'Analyze';
        }
    });

    // Allow enter key press
    tickerInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            searchBtn.click();
        }
    });
});
