from flask import Flask, request, render_template
import trio
import httpx

# Import all the platforms that Holehe supports
from holehe.modules.social_media.snapchat import snapchat
from holehe.modules.social_media.facebook import facebook
from holehe.modules.social_media.twitter import twitter
from holehe.modules.social_media.instagram import instagram
from holehe.modules.social_media.github import github
from holehe.modules.social_media.reddit import reddit
from holehe.modules.social_media.spotify import spotify
from holehe.modules.social_media.steam import steam
from holehe.modules.social_media.tumblr import tumblr
from holehe.modules.social_media.twitch import twitch
from holehe.modules.social_media.pinterest import pinterest
from holehe.modules.social_media.myspace import myspace
from holehe.modules.social_media.linkedin import linkedin

app = Flask(__name__)

# Function to run checks on all platforms
async def run_holehe(email):
    client = httpx.AsyncClient()
    result = {}

    # Snapchat check
    out_snapchat = []
    await snapchat(email, client, out_snapchat)
    result['snapchat'] = out_snapchat

    # Facebook check
    out_facebook = []
    await facebook(email, client, out_facebook)
    result['facebook'] = out_facebook

    # Twitter check
    out_twitter = []
    await twitter(email, client, out_twitter)
    result['twitter'] = out_twitter

    # Instagram check
    out_instagram = []
    await instagram(email, client, out_instagram)
    result['instagram'] = out_instagram

    # GitHub check
    out_github = []
    await github(email, client, out_github)
    result['github'] = out_github

    # Reddit check
    out_reddit = []
    await reddit(email, client, out_reddit)
    result['reddit'] = out_reddit

    # Spotify check
    out_spotify = []
    await spotify(email, client, out_spotify)
    result['spotify'] = out_spotify

    # Steam check
    out_steam = []
    await steam(email, client, out_steam)
    result['steam'] = out_steam

    # Tumblr check
    out_tumblr = []
    await tumblr(email, client, out_tumblr)
    result['tumblr'] = out_tumblr

    # Twitch check
    out_twitch = []
    await twitch(email, client, out_twitch)
    result['twitch'] = out_twitch

    # Pinterest check
    out_pinterest = []
    await pinterest(email, client, out_pinterest)
    result['pinterest'] = out_pinterest

    # MySpace check
    out_myspace = []
    await myspace(email, client, out_myspace)
    result['myspace'] = out_myspace

    # LinkedIn check
    out_linkedin = []
    await linkedin(email, client, out_linkedin)
    result['linkedin'] = out_linkedin

    # Close the HTTP client
    await client.aclose()
    return result

# Main route to display the email form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the email submission and return results
@app.route('/check_email', methods=['POST'])
async def check_email():
    email = request.form['email']
    result = await run_holehe(email)
    return render_template('results.html', result=result, email=email)

if __name__ == '__main__':
    app.run(debug=True)
    