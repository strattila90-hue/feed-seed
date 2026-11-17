const C='feedseed-v20',F=['./','index.html','manifest.json','icon-192.png','icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)));self.skipWaiting()});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!=C).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
// hálózat-első: ha van internet, mindig a legfrissebb változat töltődik be; offline a gyorsítótárból
self.addEventListener('fetch',e=>{if(e.request.method!='GET')return;e.respondWith(caches.open(C).then(c=>fetch(e.request,{cache:'no-cache'}).then(r=>{if(r&&r.ok)c.put(e.request,r.clone());return r}).catch(()=>c.match(e.request,{ignoreSearch:true}).then(m=>m||c.match('index.html')))))});
