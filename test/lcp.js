
const callback = arguments[arguments.length - 1]

setTimeout(function() {
  var lcp;
  const po = new PerformanceObserver((entryList) => {
  const entries = entryList.getEntries();
  const lastEntry = entries[entries.length - 1];

  lcp = lastEntry.renderTime || lastEntry.loadTime;
  });

  po.observe({type: 'largest-contentful-paint'});

  addEventListener('visibilitychange', function fn() {
    if (lcp && document.visibilityState === 'hidden') {
      callback(lcp)
      // removeEventListener('visibilitychange', fn, true);
    }
  }, true);


}, 12000)
