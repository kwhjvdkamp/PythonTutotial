from collections import Counter

from kwhj.kwhj_python.social_media import SocialMedia

# Tests on SocialMedia object
# -------------------------------------------------------------------
# attribute hashtag_counts
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

def test_social_media_hashtag_counts():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts

# ------------------------------------------------------------------- 
# attribute mention_counts
def test_social_media_mention_counts():
    expected_mention_counts = Counter({'learning': 1, '#python': 1, '&': 1, '#rstats': 1, 'is': 1, 'awesome!': 1, 'thanks': 1, '@datacamp!': 1})
    assert sm_post.mention_counts == expected_mention_counts