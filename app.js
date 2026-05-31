fetch('games.json')
    .then(response => response.json())
    .then(data => {
        const gameList = document.getElementById('game-list');
        data.forEach(game => {
            gameList.innerHTML += `
                <div class="game-card">
                    <h3>${game.title}</h3>
                    <p>Ölçü: ${game.size}</p>
                    <a href="${game.base}" style="color: #ffd700;">📥 Yüklə</a>
                </div>
            `;
        });
    })
    .catch(error => console.error('Xəta baş verdi:', error));