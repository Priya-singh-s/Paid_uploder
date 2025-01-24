import aiohttp
async def Master(url):
  async with aiohttp.ClientSession() as st2master:
    async with st2master.get(url, headers = {'BCOV-POLICY': "BCpkADawqM1VmXspFMod94-pT7xDCvmBEYt8U7f0mRB6XnG5huPE7I9qjhDW0qpx3LRyTD9WX7W6JvUGtgKN-qf1pJoZO-QXBMIykDivtAOgkJOmN-kyv4m_F0thrJ45z95hqWON0nsKBwvd"}) as master:
      return await master.json()

async def generate_master_url(url, auth):
    master = await Master(url)
    st2master = master["sources"]
    try:
      source = st2master[5]
    except (KeyError, IndexError):
      source = st2master[1]
    return source['src'] + "&bcov_auth=" + auth
