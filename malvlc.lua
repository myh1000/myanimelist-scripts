-- "malvlc.lua" -- VLC Extension --
function descriptor()
   return {
     title = "myanimelist VLC",
     version = "1.0",
     author = "Michael Huang",
     url = 'http://github.com/myh1000/myanimelist-scripts',
     shortdesc = "updates MAL",
     description = "updates/adds title to MAL based off title of the file.",
     capabilities = {}
   }
end

function activate()
  local input = vlc.input.item()
  local status = vlc.playlist.status()
  local clock = os.clock
  title = input:name()
  -- post("conan")
  -- local t0 = clock()
  -- while clock() - t0 <= 6 do end
  os.execute("/Applications/VLC.app/Contents/MacOS/share/lua/extensions/malpost.sh")
  vlc.deactivate()
end

function deactivate()
end

function get_anime()
  address = 'http://myanimelist.net/malappinfo.php?u=myh1000&status=all&type=anime'
  html = io.popen('wget -qO - ' .. address):read'*a'
  anime  = {}
  idx = 0
  for id in string.gmatch(html, '<series_animedb_id>.-</series_animedb_id>') do
    anime[idx] = string.match(id, '%d+')
    idx = idx + 1
  end
  return anime
end

function get_id(name)
  address = 'http://myanimelist.net/api/anime/search.xml?q=' .. name
  html = io.popen('wget -qO - ' .. address .. ' --user=username --password=password'):read'*a'
  return string.match(string.match(html, '<id>.-</id>'), '%d+')
end

function update_anime(id, episode_count)
  xml = "\'<?xml version=\"1.0\" encoding=\"UTF-8\"?><entry><episode>" .. episode_count .. "</episode><status>1</status></entry>\'"
  address='http://myanimelist.net/api/animelist/update/' .. id ..'.xml'
  data = 'data=' .. xml
  print(io.popen('wget -qO - ' .. address .. ' --user=username --password=password --post-data=' .. data):read'*a')
end

function post(title)
  local anime = get_anime()
  id = get_id(title)
  update = false
  for _,v in pairs(anime) do
    if v == id then
      update = true
      break
    end
  end
  if update then
    update_anime(id, '300')
  end
end
