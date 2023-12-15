document.getElementById('resetButton').addEventListener('click', function() {
    localStorage.clear();
    // Alternatively, to remove specific item:
    // localStorage.removeItem('yourItemKey');
});