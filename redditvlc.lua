-- "/r/anime.lua" -- VLC Extension --
function descriptor()
   return {
     title = "Open /r/anime",
     version = "1.0",
     author = "Michael Huang",
     url = 'http://github.com/myh1000/VLC-anime',
     shortdesc = "opens the /r/anime",
     description = "opens the /r/anime, in the future automatically going to the discussion pages",
     capabilities = {}
   }
end

function activate()
  local input = vlc.input.item()
  local status = vlc.playlist.status()
  if vlc.input.is_playing() and status == 'playing' then
    vlc.playlist.pause()
    os.execute("open http://reddit.com/r/anime")
  else
    os.execute("open http://reddit.com/r/anime")
  end
  vlc.deactivate()
end
function deactivate()
end
