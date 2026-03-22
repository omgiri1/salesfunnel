const CACHE='salesfunnel-v2.0';
const ASSETS=['./','./index.html','./manifest.json','./icons/icon-192x192.png','./icons/icon-512x512.png'];

self.addEventListener('install',e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener('fetch',e=>{
  // Let Firebase and Google APIs pass through
  if(e.request.url.includes('googleapis.com')||e.request.url.includes('gstatic.com')||e.request.url.includes('firebaseio.com'))return;
  e.respondWith(
    caches.match(e.request).then(r=>{
      if(r)return r;
      return fetch(e.request).then(resp=>{
        if(resp&&resp.status===200){
          const clone=resp.clone();
          caches.open(CACHE).then(c=>c.put(e.request,clone));
        }
        return resp;
      }).catch(()=>caches.match('./index.html'));
    })
  );
});
