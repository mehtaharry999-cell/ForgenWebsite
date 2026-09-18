export async function onRequest() {
  const channelId = "UCcqgxvaMTTleKbGo1xTp_tg";

  const rssUrl = `https://www.youtube.com/feeds/videos.xml?channel_id=${channelId}`;

  const response = await fetch(rssUrl);

  if (!response.ok) {
    return new Response(
      JSON.stringify({ error: "YouTube feed fetch failed" }),
      {
        status: 500,
        headers: { "Content-Type": "application/json" }
      }
    );
  }

  const xml = await response.text();

  const videoIdMatch = xml.match(
    /<yt:videoId>(.*?)<\/yt:videoId>/
  );

  const titleMatch = xml.match(
    /<media:title>(.*?)<\/media:title>/
  );

  if (!videoIdMatch) {
    return new Response(
      JSON.stringify({ error: "No video found" }),
      {
        status: 404,
        headers: { "Content-Type": "application/json" }
      }
    );
  }

  const videoId = videoIdMatch[1];
  const title = titleMatch
    ? titleMatch[1]
    : "Latest Video";

  return new Response(
    JSON.stringify({
      videoId,
      title,
      url: `https://www.youtube.com/watch?v=${videoId}`,
      thumbnail: `https://i.ytimg.com/vi/${videoId}/maxresdefault.jpg`
    }),
    {
      headers: {
        "Content-Type": "application/json",
        "Cache-Control": "public, max-age=300"
      }
    }
  );
}
