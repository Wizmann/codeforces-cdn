chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        console.log(details.url);
        if (details.url.match("http://worker.codeforces.ru")) {
            var url = details.url.replace("http://worker.codeforces.ru", "http://你的七牛云域名.com");
            return {redirectUrl: url};
        }
    },
    {urls:["http://worker.codeforces.ru/*"]},
    ["blocking"]
);
