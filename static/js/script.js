document.addEventListener('DOMContentLoaded', function() {
    // 初始化剪贴板
    new ClipboardJS('.copy-btn');

    // 为所有复制按钮添加提示
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const originalTitle = this.getAttribute('title');
            this.innerHTML = '<i class="bi bi-check"></i> 已复制';
            setTimeout(() => {
                this.innerHTML = '<i class="bi bi-clipboard"></i>';
                this.setAttribute('title', originalTitle);
            }, 2000);
        });
    });

    // 搜索功能
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const searchResults = document.getElementById('searchResults');

    function performSearch() {
        const query = searchInput.value.trim();
        if (query.length < 2) {
            searchResults.innerHTML = '<div class="list-group-item text-muted">请输入至少2个字符</div>';
            return;
        }

        fetch(`/search?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    searchResults.innerHTML = '<div class="list-group-item text-muted">没有找到匹配的公式</div>';
                    return;
                }

                searchResults.innerHTML = '';
                data.forEach(item => {
                    const resultItem = document.createElement('a');
                    resultItem.href = `#${item.category}`;
                    resultItem.className = 'list-group-item list-group-item-action';
                    resultItem.innerHTML = `
                        <strong>${item.name}</strong><br>
                        <small class="text-muted">${item.category}</small><br>
                        <code>${item.formula}</code>
                    `;
                    resultItem.addEventListener('click', function(e) {
                        // 滚动到对应位置
                        setTimeout(() => {
                            document.querySelector(`#${item.category}`).scrollIntoView({
                                behavior: 'smooth'
                            });
                        }, 100);
                    });
                    searchResults.appendChild(resultItem);
                });
            });
    }

    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keyup', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
});