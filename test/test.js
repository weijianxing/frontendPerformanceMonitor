
const callback = arguments[arguments.length - 1]
// var xhr = new XMLHttpRequest();
// xhr.open("GET", "https://www.wuage.com/", true);
// xhr.onload = function (e) {
//   if (xhr.readyState === 4) {
//     if (xhr.status === 200) {
//       console.log(xhr.responseText);
//     } else {
//       console.error(xhr.statusText);
//     }
//   }
// };
// xhr.onerror = function (e) {
//   console.error(xhr.statusText);
// };
// xhr.send(null);
// function sleep(ms) {
//   return new Promise(resolve => setTimeout(resolve, ms))
// }

function sleep(ms) {
  return new Promise(resolve =>
      setTimeout(resolve, ms)
  )
}
// sleep(3000).then(()=>{
   //code
// })

setTimeout(function() {
    //relaod wuage.com
    entries = window.performance.getEntries()
    // window.location.href="www.wuage.com";
    window.onload = function () {window.location.reload()}
    var entiries_arry = []

    for (i = 0; i < 7; i++) {
            // sleep(300)
            sleep(300).then(()=>{
             entries = window.performance.getEntries()
            entiries_arry.push(entries)
        })
    }
    callback(entiries_arry)
}, 12000)
