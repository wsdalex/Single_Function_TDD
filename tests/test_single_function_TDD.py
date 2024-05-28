from lib.single_function_TDD import *

def test_200_word_text():
    result = calc_reading_time('''
In the bustling city of Everbrook, nestled between towering skyscrapers and busy streets, lies a hidden gem called Harmony Park. This quaint oasis, often overlooked by the city's hurried inhabitants, offers a serene escape from the chaos of urban life. The park, established in the early 1900s, is a testament to nature's resilience and beauty amidst concrete and steel.

Walking through its winding paths, one is greeted by the gentle rustling of leaves and the melodious chirping of birds. The centerpiece of Harmony Park is a sparkling pond, where ducks and swans glide gracefully across the water's surface. Benches are strategically placed under the shade of ancient oak trees, inviting visitors to sit and soak in the tranquil atmosphere.

Every spring, the park bursts into a riot of colors as flowers bloom, filling the air with a sweet, intoxicating fragrance. Children can often be seen playing on the well-maintained playground, their laughter adding a joyful soundtrack to the peaceful surroundings. Nearby, a small café serves freshly brewed coffee and homemade pastries, providing a perfect spot for relaxation.

Harmony Park, though small, is a cherished refuge, reminding everyone who visits of the simple, enduring beauty of nature.
                            ''')
    assert result == 'It will take 1 minute to read this text.'

def test_600_word_text():
    result = calc_reading_time("In the midst of chaos, there lies a whisper of serenity, a momentary pause in the relentless march of time. It's in these fleeting instances that we find ourselves caught between the echoes of our past and the uncertainty of our future. Like grains of sand slipping through the hourglass, each passing second carries with it the weight of infinite possibilities, yet we are bound by the constraints of our own perceptions. Life, they say, is a journey—a winding path that leads us through valleys of despair and peaks of euphoria. Along the way, we encounter strangers who become friends, and friends who become strangers. We stumble, we fall, but we rise again, our spirits tempered by the trials of our existence. In the dance of existence, every step is a choice, every movement a reflection of our innermost desires. We paint the canvas of our lives with the brushstrokes of experience, weaving a tapestry of memories that define who we are. And yet, for all our striving, we are but players on a stage, reciting lines written by a cosmic playwright. But perhaps therein lies the beauty of it all—the realization that we are not alone, that our stories are but threads in the fabric of the universe. From the ashes of our struggles rise the seeds of hope, nourished by the gentle rains of compassion and understanding. And though the road may be long and arduous, we press on, guided by the light of our dreams. In the silence of the night, when the world sleeps and the stars whisper secrets to the moon, we find solace in the knowledge that we are part of something greater than ourselves. It is in this moment of quiet contemplation that we glimpse the true nature of our existence—a tapestry of interconnectedness, woven together by the threads of love and empathy. And so, as we navigate the labyrinth of life, let us remember that every encounter, every interaction, is an opportunity to spread kindness and joy. For in giving, we receive, and in loving, we are loved in return. And though the road may be fraught with obstacles, we walk it together, hand in hand, hearts ablaze with the fire of possibility. As the sun rises on a new day, let us greet it with open arms and open hearts, embracing the beauty of the unknown. For in the vast expanse of the universe, we are but specks of stardust, fleeting and ephemeral. And yet, in our insignificance lies our greatest strength—for it is only when we surrender to the flow of existence that we truly find ourselves. So let us dance to the rhythm of life, our souls entwined in a symphony of love and laughter. For in the end, it is not the destination that matters, but the journey itself—the moments of joy, the tears of sorrow, and everything in between. And though we may never unravel the mysteries of the universe, we can take comfort in the knowledge that we are part of its grand design.")
    assert result == 'It will take 3 minutes to read this text.'

def test_40_word_text():
    result = calc_reading_time("Harmony Park, a serene oasis in Everbrook, offers a peaceful escape with its winding paths, blooming flowers, and a sparkling pond. Benches under oak trees and a quaint café invite visitors to relax and enjoy nature's beauty amidst urban life.")
    assert result == 'It will take 1 minute to read this text.'

def test_if_minutes_round_up_correctly():
    result = calc_reading_time("In the heart of the vibrant city of Everbrook, amidst its towering skyscrapers and bustling streets, lies an enchanting sanctuary known as Harmony Park. This quaint oasis, often overlooked by the city's hurried inhabitants, offers a serene escape from the relentless pace of urban life. Established in the early 1900s, the park stands as a testament to nature's resilience and enduring beauty amidst the concrete jungle. As you walk through its winding paths, the gentle rustling of leaves and the melodious chirping of birds greet you, creating a soothing symphony that contrasts sharply with the city's constant hum. The centerpiece of Harmony Park is a sparkling pond, where ducks and swans glide gracefully across the water's surface, leaving gentle ripples in their wake. Benches are strategically placed under the shade of ancient oak trees, inviting visitors to sit and soak in the tranquil atmosphere, far removed from the hustle and bustle just beyond the park's boundaries. Every spring, Harmony Park bursts into a riot of colors as flowers of various hues bloom, filling the air with a sweet, intoxicating fragrance. Tulips, daffodils, and cherry blossoms create a breathtaking tapestry that delights the senses and lifts the spirits. The park's meticulously maintained flower beds and manicured lawns are a testament to the dedication of the city’s gardeners, who work tirelessly to preserve this haven of natural beauty. Children can often be seen playing on the well-maintained playground, their laughter adding a joyful soundtrack to the peaceful surroundings. The playground, equipped with swings, slides, and climbing structures, provides a safe and fun environment for kids to explore and expend their boundless energy. Nearby, a small café serves freshly brewed coffee and homemade pastries, offering a perfect spot for relaxation. Patrons can enjoy their refreshments at outdoor tables, shaded by colorful umbrellas, while watching the world go by. Harmony Park is also home to a charming gazebo, often used for community events such as concerts, weddings, and art exhibitions. On weekends, local musicians and bands perform here, their melodies blending harmoniously with the natural sounds of the park.")
    assert result == 'It will take 2 minutes to read this text.'

def test_correct_grammar_text():
    result = grammar_check('Hello, my name is Will!')
    assert result == True

def test_no_capital_on_first_word():
    result = grammar_check('hello, my name is Will!')
    assert result == False

def test_no_sentence_ender():
    result = grammar_check('Hello, my name is Will1')
    assert result == False

def test_another_correct_text():
    result = grammar_check('Good morning! It is nice to see you today.')