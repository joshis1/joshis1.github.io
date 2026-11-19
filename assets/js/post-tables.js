for (const table of document.querySelectorAll('.post-content table')) {
  if (table.closest('.practice-matrix')) continue;

  const wrapper = document.createElement('div');
  wrapper.className = 'post-table';
  wrapper.tabIndex = 0;
  wrapper.setAttribute('role', 'region');
  wrapper.setAttribute('aria-label', table.caption?.textContent.trim() || 'Article table');
  table.before(wrapper);
  wrapper.append(table);
}
