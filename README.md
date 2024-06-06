<img src="https://github.com/KaiyuSugiyama/playlistapp/assets/71801717/2b8a61b8-b2ad-4a74-985e-dc5e56328064">

)
# Playlist Website!
Project for tri3
### Links
- [Website](http://127.0.0.1:5000/)
- [Project Plan](https://docs.google.com/document/d/1VhrjKwS2le839EvtZD7INS6q4-S92xcqoazgZcf71jE/edit)

### Collaborators
- Jake Shim
- Kaiyu Sugiyama 
# How It's Made
## Theme Section (5pt)
    - This page demonstrates usage and display of [online APIs that take parametrs]
    - Users can input an Artist and the Track name as well as how they want the list sorted. The response displays song cards that the user can listen to. These cares provide info such as wear to listen and popularity info.
    - As a music-focused site, this page helps users find new songs if they ever want new songs that are similar to the ones they are currently listening to
- Database 
    - This code shows the database that takes the user input from the submit form and connects it to our API, which our site sends request to using ajax.
- OUR API (+0.5 Technical)
    - Serves data that drives our site, devs can access all user submitted data/playlists with a plethora of different endpoints.
    - 5 different endpoints. [backend code](https://github.com/KaiyuSugiyama/playlistapp/tree/main/templates)
    - Serves as our API that other teams can use for crossover
## API Section 
- [API Endpoints](https://playlist.nighthawkcodingsociety.com/api/) ([Receiving](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20)  API
- ![image](http://owo.whats-th.is/8NTno86.png)
    - [Source Code](https://github.com/zenxha/kpop/blob/main/view/api/app.py)
    - API serves data that drives our site to anyone in the form of JSON
    - API for finding songs is used [here](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20-L38) and song data is stored as a class 
## Deployment Section 
- The site is not deployed yet. It will be done by the end of this year.
