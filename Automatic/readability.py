import textacy
from textacy import text_stats as ts
import csv

def print_scores(dc, writer):
    '''Takes sentences as input and calculates the reading ease for every sentence with the conversation context.
    Takes a csv writer object to write all to a csv file.'''
    for key in dc:
        text = dc[key]
        doc = textacy.make_spacy_doc(text, lang="en_core_web_sm")
        scores = [key, ts.flesch_reading_ease(doc)]

        writer.writerow(scores)

def main():
    list_of_scores = []
    header = ['line', 'Flesch reading ease']
    f = open('readabilityFlesch.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)

    C1_R = {'C1_R1_R':"And at least one from a housekeeper."
                " I really want to see this Maury episode."
                " I would pay money to see someone edit together such a thing.",
                'C1_R2_R': "And at least one from a housekeeper."
                           " I really want to see this Maury episode."
                           " It's a great show.",
                'C1_R3_R': "And at least one from a housekeeper."
                           " I really want to see this Maury episode."
                           " I don't get it.",
                'C1_R4_R': "And at least one from a housekeeper."
                           " I really want to see this Maury episode."
                           " I want to see this episode."
                }
    print_scores(C1_R, writer)


    C2_R = {'C2_R1_R':"What is your most successful unethical life hack?"
                " If you have siblings, blame them for everything"
                " Unless they are more successful than you, then have a good relationship and take the blame for everything.",
                'C2_R2_R': "What is your most successful unethical life hack?"
                           " If you have siblings, blame them for everything"
                           " I don't know what you are talking about.",
                'C2_R3_R': "What is your most successful unethical life hack?"
                           " If you have siblings, blame them for everything"
                           " I dont'know if you are being sarcastic or not.",
                'C2_R4_R': "What is your most successful unethical life hack?"
                           " If you have siblings, blame them for everything"
                           " what if you don't have kids?"
                }
    print_scores(C2_R, writer)

    C3_R = {'C3_R1_R': "I am not convinced he 's coming back"
                " not going to happen. that would be crazy if it did though . what would happen?"
                " I am not sure if that is a thing or not.",
                'C3_R2_R': "I am not convinced he 's coming back"
                           " not going to happen. that would be crazy if it did though . what would happen?"
                           " I don't know, but I think he is going to be a lot worse.",
                'C3_R3_R': "I am not convinced he 's coming back"
                           " not going to happen. that would be crazy if it did though . what would happen?"
                           " I'm sure he 'll be fine.",
                'C3_R4_R': "I am not convinced he 's coming back"
                           " not going to happen. that would be crazy if it did though . what would happen?"
                           " if the president refused to return? the GOP would definitely impeach him and accept pence."
                }
    print_scores(C3_R, writer)

    C4_R = {'C4_R1_R': "what fact are you tired of explaining to people? "
                " no, I am not cheating on my husband, and no, neither of us pressured the other into this. Healthy and consensual nonmonogamy is a thing."
                " sounds more like you are cheating on your husband.",
                'C4_R2_R': "what fact are you tired of explaining to people? "
                           " no, I am not cheating on my husband, and no, neither of us pressured the other into this. Healthy and consensual nonmonogamy is a thing."
                           " I am sorry to hear that",
                'C4_R3_R': "what fact are you tired of explaining to people? "
                           " no, I am not cheating on my husband, and no, neither of us pressured the other into this. Healthy and consensual nonmonogamy is a thing."
                           " I don't believe you.",
                'C4_R4_R': "what fact are you tired of explaining to people? "
                           " no, I am not cheating on my husband, and no, neither of us pressured the other into this. Healthy and consensual nonmonogamy is a thing."
                           " I don't think you understand what you are talking about."
                }
    print_scores(C4_R, writer)

    C5_R = {'C5_R1_R': "What supporting character from a tv show would you definitely watch in their own spinoff?"
                " the adventures of creed bratton"
                " Eh. Creed worked because they made sure not to overuse him. I think his shock value would get pretty old in a show of nothing but him.",
                'C5_R2_R': "What supporting character from a tv show would you definitely watch in their own spinoff?"
                           " the adventures of creed bratton"
                           " I don't get it.",
                'C5_R3_R': "What supporting character from a tv show would you definitely watch in their own spinoff?"
                           " the adventures of creed bratton"
                           " I would love to see him as a villain.",
                'C5_R4_R': "What supporting character from a tv show would you definitely watch in their own spinoff?"
                           " the adventures of creed bratton"
                           " Creed Bratton is the best actor of all time."
                }
    print_scores(C5_R, writer)

    C6_R = {'C6_R1_R': "His tweets are really entertaining tbh. scary and absurd, but entertaining."
                           " I simply can not look away. it just keeps getting weirder."
                           " I'm not sure if you are being sarcastic or not.",
                'C6_R2_R': "His tweets are really entertaining tbh. scary and absurd, but entertaining."
                           " I simply can not look away. it just keeps getting weirder."
                           " Bizarro America is a strange show.",
                'C6_R3_R': "His tweets are really entertaining tbh. scary and absurd, but entertaining."
                           " I simply can not look away. it just keeps getting weirder."
                           " I don't get it.",
                'C6_R4_R': "His tweets are really entertaining tbh. scary and absurd, but entertaining."
                           " I simply can not look away. it just keeps getting weirder."
                           " I think it is a bit of a stretch."
                }
    print_scores(C6_R, writer)

    C7_R = {'C7_R1_R': "I am stealing this thank you very much."
                           " I made this."
                           " well then I'm still stealing it, thank you very much.",
                'C7_R2_R': "I am stealing this thank you very much."
                           " I made this."
                           " I third this",
                'C7_R3_R': "I am stealing this thank you very much."
                           " I made this."
                           " I made this.",
                'C7_R4_R': "I am stealing this thank you very much."
                           " I made this."
                           " you made this?"
                }
    print_scores(C7_R, writer)

    C8_R = {'C8_R1_R': "Reminds me of how there are more plastic flamingos than real ones"
                           " Plastic flamingos in the front yard is a sign that swingers live there. so they are more swingers than real flamingos?"
                           " plastic flamingos?",
                'C8_R2_R': "Reminds me of how there are more plastic flamingos than real ones"
                           " Plastic flamingos in the front yard is a sign that swingers live there. so they are more swingers than real flamingos?"
                           " no, it is just a plastic bag.",
                'C8_R3_R': "Reminds me of how there are more plastic flamingos than real ones"
                           " Plastic flamingos in the front yard is a sign that swingers live there. so they are more swingers than real flamingos?"
                           " I have never heard of that. I have never heard of it.",
                'C8_R4_R': "Reminds me of how there are more plastic flamingos than real ones"
                           " Plastic flamingos in the front yard is a sign that swingers live there. so they are more swingers than real flamingos?"
                           " I guess that explains Florida?"
                }
    print_scores(C8_R, writer)

    C9_R = {'C9_R1_R': "keep him as Erick and keep McAvoy as Charles but for the love of god give everyone else a do-over."
                           " would love this, but if I had to pick another to differentiate from the fox , Nikolaj Coster - waldau seems like a great choice"
                           " I would love to see him as a villain.",
                'C9_R2_R': "keep him as Erick and keep McAvoy as Charles but for the love of god give everyone else a do-over."
                           " would love this, but if I had to pick another to differentiate from the fox , Nikolaj Coster - waldau seems like a great choice"
                           " I would love to see him play the role of doom.",
                'C9_R3_R': "keep him as Erick and keep McAvoy as Charles but for the love of god give everyone else a do-over."
                           " would love this, but if I had to pick another to differentiate from the fox , Nikolaj Coster - waldau seems like a great choice"
                           " Isn't that Jamie from got? I could see him killing that roll",
                'C9_R4_R': "keep him as Erick and keep McAvoy as Charles but for the love of god give everyone else a do-over."
                           " would love this, but if I had to pick another to differentiate from the fox , Nikolaj Coster - waldau seems like a great choice"
                           " I am not sure what you are trying to say."
                }
    print_scores(C9_R, writer)

    C10_R = {'C10_R1_R': "Yeah he healed his wound with his spray thing, the same one he used to seal the door."
                           " He would have been if doctor strange did not give Thanos the time stone "
                           " does this happen on Titan?",
                'C10_R2_R': "Yeah he healed his wound with his spray thing, the same one he used to seal the door."
                           " He would have been if doctor strange did not give Thanos the time stone "
                           " that's what I thought, but I don't think that's how it works.",
                'C10_R3_R': "Yeah he healed his wound with his spray thing, the same one he used to seal the door."
                           " He would have been if doctor strange did not give Thanos the time stone "
                           " He did not have the power to do that.",
                'C10_R4_R': "Yeah he healed his wound with his spray thing, the same one he used to seal the door."
                           " He would have been if doctor strange did not give Thanos the time stone "
                           " I think it is time to rewatch the gauntlet."
                }
    print_scores(C10_R, writer)

    C11_R = {'C11_R1_R': "The inevitable moment"
                           " Isn't that the guy that lost the British election against the idiot that initiated the Brexit referendum?"
                           " Ed Miliband",
                'C11_R2_R': "The inevitable moment"
                           " Isn't that the guy that lost the British election against the idiot that initiated the Brexit referendum?"
                           " No, it was a joke.",
                'C11_R3_R': "The inevitable moment"
                           " Isn't that the guy that lost the British election against the idiot that initiated the Brexit referendum?"
                           " no, that 's the guy who voted for Brexit.",
                'C11_R4_R': "The inevitable moment"
                           " Isn't that the guy that lost the British election against the idiot that initiated the Brexit referendum?"
                           " no, that was the referendum."
                }
    print_scores(C11_R, writer)

    C12_R = {'C12_R1_R': "what do they taste like?"
                           " A camel scotch fillet is marbled like good beef, except triple the size. the flavor is very much like beef - slightly stronger but very delicious."
                           " Camel is now on my 'eat' list. I still have not eaten a venison steak",
                'C12_R2_R': "what do they taste like?"
                           " A camel scotch fillet is marbled like good beef, except triple the size. the flavor is very much like beef - slightly stronger but very delicious."
                           " I've never heard of this before. what's it about?",
                'C12_R3_R': "what do they taste like?"
                           " A camel scotch fillet is marbled like good beef, except triple the size. the flavor is very much like beef - slightly stronger but very delicious."
                           " I've never heard of that. what's it taste like?",
                'C12_R4_R': "what do they taste like?"
                           " A camel scotch fillet is marbled like good beef, except triple the size. the flavor is very much like beef - slightly stronger but very delicious."
                           " What is the difference?"
                }
    print_scores(C12_R, writer)

    C13_R = {'C13_R1_R': "what will become illegal in the next 50 years?"
                           " driving a manual car on a public road."
                           " I don't think that is illegal.",
                'C13_R2_R': "what will become illegal in the next 50 years?"
                           " driving a manual car on a public road."
                           " do you mean manual as in 'manual transmission' or manual as in 'human operated'?",
                'C13_R3_R': "what will become illegal in the next 50 years?"
                           " driving a manual car on a public road."
                           " I don't get it.",
                'C13_R4_R': "what will become illegal in the next 50 years?"
                           " driving a manual car on a public road."
                           " what if it is already illegal?"
                }
    print_scores(C13_R, writer)

    C14_R = {'C14_R1_R': "back when he was the 'happy one'"
                           " mou has changed so much now. it 's unfortunate that he has."
                           " He has not changed, he has always had the same mood swings over the years.",
                'C14_R2_R': "back when he was the 'happy one'"
                           " mou has changed so much now. it 's unfortunate that he has."
                           " I'm not sure what you 're trying to say.",
                'C14_R3_R': "back when he was the 'happy one'"
                           " mou has changed so much now. it 's unfortunate that he has."
                           " yeah, he has been pretty good in the past few years.",
                'C14_R4_R': "back when he was the 'happy one'"
                           " mou has changed so much now. it 's unfortunate that he has."
                           " I think he is the best player in the league."
                }
    print_scores(C14_R, writer)


    C15_R = {'C15_R1_R': "what two videogames would you like to see in a crossover game?"
                           " total war star wars"
                           " I think star wars and company of heroes or dawn of war would be a better fit. the cover system, unit groups, vehicles, etc. plus the delicious physics.",
                'C15_R2_R': "what two videogames would you like to see in a crossover game?"
                           " total war star wars"
                           " I'm not sure what you mean by that.",
                'C15_R3_R': "what two videogames would you like to see in a crossover game?"
                           " total war star wars"
                           " that would be awesome.",
                'C15_R4_R': "what two videogames would you like to see in a crossover game?"
                           " total war star wars"
                           " star wars?"
                }
    print_scores(C15_R, writer)

    C16_R = {'C16_R1_R': "wherever you go, there you are."
                           " what is this a quote from?"
                           " I hear it in aa. I don't know the original origin.",
                'C16_R2_R': "wherever you go, there you are."
                           " what is this a quote from?"
                           " it is a reference to something like this : URL",
                'C16_R3_R': "wherever you go, there you are."
                           " what is this a quote from?"
                           " It is a quote from arrested development.",
                'C16_R4_R': "wherever you go, there you are."
                           " what is this a quote from?"
                           " it is a quote from the office."
                }
    print_scores(C16_R, writer)

    C17_R = {'C17_R1_R': "what are some real facts that sound fake at first?"
                           " roughly 70 % of the world's oxygen is produced by marine algae."
                           " 26 % of the worlds hot air is produced by politicians.",
                'C17_R2_R': "what are some real facts that sound fake at first?"
                           " roughly 70 % of the world's oxygen is produced by marine algae."
                           " that is not true at all.",
                'C17_R3_R': "what are some real facts that sound fake at first?"
                           " roughly 70 % of the world's oxygen is produced by marine algae."
                           " I'm pretty sure that is a myth.",
                'C17_R4_R': "what are some real facts that sound fake at first?"
                           " roughly 70 % of the world's oxygen is produced by marine algae."
                           " I don't believe you."
                }
    print_scores(C17_R, writer)

    C18_R = {'C18_R1_R': "what is the most NSFW thing you have seen at an office gathering or party?"
                           " A coworker once stood on a swivel chair"
                           " officer buckle and Gloria would not be happy",
                'C18_R2_R': "what is the most NSFW thing you have seen at an office gathering or party?"
                           " A coworker once stood on a swivel chair"
                           " that is a good one.",
                'C18_R3_R': "what is the most NSFW thing you have seen at an office gathering or party?"
                           " A coworker once stood on a swivel chair"
                           " how did you find out?",
                'C18_R4_R': "what is the most NSFW thing you have seen at an office gathering or party?"
                           " A coworker once stood on a swivel chair"
                           " What was on the chair?"
                }
    print_scores(C18_R, writer)

    C19_R = {'C19_R1_R': "homemade my sister's specialty, carrot cake"
                           " recipe?"
                           " here is the recipe",
                'C19_R2_R': "homemade my sister's specialty, carrot cake"
                           " recipe?"
                           " here you go",
                'C19_R3_R': "homemade my sister's specialty, carrot cake"
                           " recipe?"
                           " I'll give it a try!",
                'C19_R4_R': "homemade my sister's specialty, carrot cake"
                           " recipe?"
                           " remind me ! 2 days"
                }
    print_scores(C19_R, writer)

    C20_R = {'C20_R1_R': "I ran 3 miles today thinking that was 5 km I was so hyped because I did not walk at all then I look at my Nike run achievement and 5 km equal 3.1 miles"
                           " this just gave me a weird thought, is there a metric version of the term mileage ? or is that a universal term ? or am I just an idiot?"
                           " this is a good question",
                'C20_R2_R': "I ran 3 miles today thinking that was 5 km I was so hyped because I did not walk at all then I look at my Nike run achievement and 5 km equal 3.1 miles"
                           " this just gave me a weird thought, is there a metric version of the term mileage ? or is that a universal term ? or am I just an idiot?"
                           " that is what I was going to say.",
                'C20_R3_R': "I ran 3 miles today thinking that was 5 km I was so hyped because I did not walk at all then I look at my Nike run achievement and 5 km equal 3.1 miles"
                           " this just gave me a weird thought, is there a metric version of the term mileage ? or is that a universal term ? or am I just an idiot?"
                           " I think it is called 'measurement'",
                'C20_R4_R': "I ran 3 miles today thinking that was 5 km I was so hyped because I did not walk at all then I look at my Nike run achievement and 5 km equal 3.1 miles"
                           " this just gave me a weird thought, is there a metric version of the term mileage ? or is that a universal term ? or am I just an idiot?"
                           " it is a unit of measurement."
                }
    print_scores(C20_R, writer)

    C21_R = {'C21_R1_R': "literally the best team possible. I will never forget how good that show is."
                           " I just watched it for the first time a few weeks ago. I wish I could re-experience it over again."
                           " my husband and I found it on amazon prime. we binge watched it with the self-control of weight watchers meeting next to a bakery.",
                'C21_R2_R': "literally the best team possible. I will never forget how good that show is."
                           " I just watched it for the first time a few weeks ago. I wish I could re-experience it over again."
                           " I have not watched it yet, but I have never seen it. I'll check it out.",
                'C21_R3_R': "literally the best team possible. I will never forget how good that show is."
                           " I just watched it for the first time a few weeks ago. I wish I could re-experience it over again."
                           " It's a great show, but it's a great show.",
                'C21_R4_R': "literally the best team possible. I will never forget how good that show is."
                           " I just watched it for the first time a few weeks ago. I wish I could re-experience it over again."
                           " I watched the first season. it was amazing."
                }
    print_scores(C21_R, writer)

    C22_R = {'C22_R1_R': "what kind of bear is Paddington?"
                           " spectacled bear. he does n't really look like one, but he 's from Peru, and that 's the only species of bear that lives there"
                           " thank you very much for the response.",
                'C22_R2_R': "what kind of bear is Paddington?"
                           " spectacled bear. he does n't really look like one, but he 's from Peru, and that 's the only species of bear that lives there"
                           " I don't know what that is, but I'm not sure what you 're trying to say.",
                'C22_R3_R': "what kind of bear is Paddington?"
                           " spectacled bear. he does n't really look like one, but he 's from Peru, and that 's the only species of bear that lives there"
                           " that is not a polar bear.",
                'C22_R4_R': "what kind of bear is Paddington?"
                           " spectacled bear. he does n't really look like one, but he 's from Peru, and that 's the only species of bear that lives there"
                           " I thought he was a bear?"
                }
    print_scores(C22_R, writer)

    C23_R = {'C23_R1_R': "are you living in some other timeline? and if so, can you smuggle me over there?"
                           " they are talking about the popular vote. in terms of the popular vote, Hillary had about a million more votes than Donald Trump"
                           " over 2 million more you mean?",
                'C23_R2_R': "are you living in some other timeline? and if so, can you smuggle me over there?"
                           " they are talking about the popular vote. in terms of the popular vote, Hillary had about a million more votes than Donald Trump"
                           " that is not what I said.",
                'C23_R3_R': "are you living in some other timeline? and if so, can you smuggle me over there?"
                           " they are talking about the popular vote. in terms of the popular vote, Hillary had about a million more votes than Donald Trump"
                           " the popular vote does not matter.",
                'C23_R4_R': "are you living in some other timeline? and if so, can you smuggle me over there?"
                           " they are talking about the popular vote. in terms of the popular vote, Hillary had about a million more votes than Donald Trump"
                           " that is not how elections work."
                }
    print_scores(C23_R, writer)

    C24_R = {'C24_R1_R': "let it cool, it 'll be the only metal colored thing there"
                           " actually, it will probably be black and covered with soot. it wo n't really stand out that much among all the ash."
                           " magnet. already posted above this.",
                'C24_R2_R': "let it cool, it 'll be the only metal colored thing there"
                           " actually, it will probably be black and covered with soot. it wo n't really stand out that much among all the ash."
                           " that is what I was thinking, but I'm not sure what you mean by that.",
                'C24_R3_R': "let it cool, it 'll be the only metal colored thing there"
                           " actually, it will probably be black and covered with soot. it wo n't really stand out that much among all the ash."
                           " that is what I was thinking, but I'm not sure what you mean by that.",
                'C24_R4_R': "let it cool, it 'll be the only metal colored thing there"
                           " actually, it will probably be black and covered with soot. it wo n't really stand out that much among all the ash."
                           " yeah, but it 's not black and white."
                }
    print_scores(C24_R, writer)

    C25_R = {'C25_R1_R': "tabs or spaces?"
                           " the real question is tab - size."
                           " I think you meant spaces.",
                'C25_R2_R': "tabs or spaces?"
                           " the real question is tab - size."
                           " I thought it was the same thing.",
                'C25_R3_R': "tabs or spaces?"
                           " the real question is tab - size."
                           " what is the difference between the two?",
                'C25_R4_R': "tabs or spaces?"
                           " the real question is tab - size."
                           " yeah, is it common to have something else than 4 spaces?"
                }
    print_scores(C25_R, writer)

    C26_R = {'C26_R1_R': "but it worked for Turris! Jesus, I miss that guy he was supposed to be my sweater this Christmas."
                           " I miss him too but he was n't signing with the team so we had to trade him. Hoffman is under contract . does not make sense to move him."
                           " what does not make sense is letting Dorion be in charge of a rebuild?",
                'C26_R2_R': "but it worked for Turris! Jesus, I miss that guy he was supposed to be my sweater this Christmas."
                           " I miss him too but he was n't signing with the team so we had to trade him. Hoffman is under contract . does not make sense to move him."
                           " he was the only one who did not get the joke.",
                'C26_R3_R': "but it worked for Turris! Jesus, I miss that guy he was supposed to be my sweater this Christmas."
                           " I miss him too but he was n't signing with the team so we had to trade him. Hoffman is under contract . does not make sense to move him."
                           " I think it was a joke, but I don't think it's worth it.",
                'C26_R4_R': "but it worked for Turris! Jesus, I miss that guy he was supposed to be my sweater this Christmas."
                           " I miss him too but he was n't signing with the team so we had to trade him. Hoffman is under contract . does not make sense to move him."
                           " yeah, but he is still on the bench."
                }
    print_scores(C26_R, writer)

    C27_R = {'C27_R1_R': "who are you and what have you done today?"
                           " I'm just a lowly security guard, sitting in a guard shack since 6 am. two more hours. two more hours."
                           " that is a cool job, man . don't put yourself down. you 're not lowly. that 's an awesome job to have.",
                'C27_R2_R': "who are you and what have you done today?"
                           " I'm just a lowly security guard, sitting in a guard shack since 6 am. two more hours. two more hours."
                           " what kind of job?",
                'C27_R3_R': "who are you and what have you done today?"
                           " I'm just a lowly security guard, sitting in a guard shack since 6 am. two more hours. two more hours."
                           " good luck!",
                'C27_R4_R': "who are you and what have you done today?"
                           " I'm just a lowly security guard, sitting in a guard shack since 6 am. two more hours. two more hours."
                           " what is your job?"
                }
    print_scores(C27_R, writer)

    C28_R = {'C28_R1_R': "he would be fine in the right setting, North Korea, Saudi Arabia, Alabama."
                           " can we vote to send him somewhere else?"
                           " like Texas?",
                'C28_R2_R': "he would be fine in the right setting, North Korea, Saudi Arabia, Alabama."
                           " can we vote to send him somewhere else?"
                           " no, he will be president.",
                'C28_R3_R': "he would be fine in the right setting, North Korea, Saudi Arabia, Alabama."
                           " can we vote to send him somewhere else?"
                           " I don't think so.",
                'C28_R4_R': "he would be fine in the right setting, North Korea, Saudi Arabia, Alabama."
                           " can we vote to send him somewhere else?"
                           " he is already in office."
                }
    print_scores(C28_R, writer)

    C29_R = {'C29_R1_R': "can't run as fast on a bike."
                           " the bike was two - tired."
                           " I thought it was funny.",
                'C29_R2_R': "can't run as fast on a bike."
                           " the bike was two - tired."
                           " that is not how it works.",
                'C29_R3_R': "can't run as fast on a bike."
                           " the bike was two - tired."
                           " that is what I was thinking.",
                'C29_R4_R': "can't run as fast on a bike."
                           " the bike was two - tired."
                           " finally, all of those bazooka joe comics, and 1980 's joke books paid off ! this was brilliant btw."
                }
    print_scores(C29_R, writer)

    C30_R = {'C30_R1_R': "a dominos employee stood outside of recently closed papa john in my neighborhood and started selling some pizzas."
                           " wait wtf , since when did the papa john's down in bay ridge close?"
                           " it's been a while since I've seen it.",
                'C30_R2_R': "a dominos employee stood outside of recently closed papa john in my neighborhood and started selling some pizzas."
                           " wait wtf , since when did the papa john's down in bay ridge close?"
                           " I don't know, I've never heard of papa johns.",
                'C30_R3_R': "a dominos employee stood outside of recently closed papa john in my neighborhood and started selling some pizzas."
                           " wait wtf , since when did the papa john's down in bay ridge close?"
                           " I'm not sure what you are trying to say.",
                'C30_R4_R': "a dominos employee stood outside of recently closed papa john in my neighborhood and started selling some pizzas."
                           " wait wtf , since when did the papa john's down in bay ridge close?"
                           " it is been like a week"
                }
    print_scores(C30_R, writer)

    C31_R = {'C31_R1_R': "do it, bro. get stoned and swim with the sharks."
                           " do you think they 'll know I'm high like cats do?"
                           " ehhh. They might have their suspicions.",
                'C31_R2_R': "do it, bro. get stoned and swim with the sharks."
                           " do you think they 'll know I'm high like cats do?"
                           " don't worry, you'll be fine.",
                'C31_R3_R': "do it, bro. get stoned and swim with the sharks."
                           " do you think they 'll know I'm high like cats do?"
                           " do you have cats?",
                'C31_R4_R': "do it, bro. get stoned and swim with the sharks."
                           " do you think they 'll know I'm high like cats do?"
                           " if you don't like them, you'll be fine."
                }
    print_scores(C31_R, writer)

    C32_R = {'C32_R1_R': "then he got super hunky towards the end. basically like trying to believe that Channing Tatum could ever possibly play someone who can't get laid."
                           " you got a picture? I can't imagine hunky Urkel."
                           " google?",
                'C32_R2_R': "then he got super hunky towards the end. basically like trying to believe that Channing Tatum could ever possibly play someone who can't get laid."
                           " you got a picture? I can't imagine hunky Urkel."
                           " I don't think I've ever seen him in a movie.",
                'C32_R3_R': "then he got super hunky towards the end. basically like trying to believe that Channing Tatum could ever possibly play someone who can't get laid."
                           " you got a picture? I can't imagine hunky Urkel."
                           " here you go",
                'C32_R4_R': "then he got super hunky towards the end. basically like trying to believe that Channing Tatum could ever possibly play someone who can't get laid."
                           " you got a picture? I can't imagine hunky Urkel."
                           " I don't think I've ever seen a picture of him before."
                }
    print_scores(C32_R, writer)

    C33_R = {'C33_R1_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " chucked $5 on Ricciardo top 3 finish for more fun haha",
                'C33_R2_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " thanks! I'll have to check it out!",
                'C33_R3_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " these are my favorite pair of all time.",
                'C33_R4_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " I'm not sure if this is a typo or not."
                }
    print_scores(C33_R, writer)

    C34_R = {'C34_R1_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " chucked $5 on Ricciardo top 3 finish for more fun haha",
                'C34_R2_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " I have not seen it yet, but I'll check it out. thanks!",
                'C34_R3_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " thanks! I'll check it out!",
                'C34_R4_R': "first time watching f1!"
                           " enjoy the show! unfortunately, Monaco can be a bit of a parade sometimes, I hope it gets interesting so you have a nice first race!"
                           " thanks!"
                }
    print_scores(C34_R, writer)

    C35_R = {'C35_R1_R': "we should collect all of the trash in the world, turn it into a ball, and fling it all into space."
                           " what if it comes back in 1000 years?"
                           " that's 10 generations away, who cares!",
                'C35_R2_R': "we should collect all of the trash in the world, turn it into a ball, and fling it all into space."
                           " what if it comes back in 1000 years?"
                           " then we can build a wall.",
                'C35_R3_R': "we should collect all of the trash in the world, turn it into a ball, and fling it all into space."
                           " what if it comes back in 1000 years?"
                           " then you would have to go to the moon.",
                'C35_R4_R': "we should collect all of the trash in the world, turn it into a ball, and fling it all into space."
                           " what if it comes back in 1000 years?"
                           " what if the earth is flat?"
                }
    print_scores(C35_R, writer)

    C36_R = {'C36_R1_R': "I could say the same to you man"
                           " you must be fun at parties"
                           " 'just leave it' continues to reply",
                'C36_R2_R': "I could say the same to you man"
                           " you must be fun at parties"
                           " I'm not your buddy, pal.",
                'C36_R3_R': "I could say the same to you man"
                           " you must be fun at parties"
                           " you must be fun at parties",
                'C36_R4_R': "I could say the same to you man"
                           " you must be fun at parties"
                           " I don't think you're fun at parties"
                }
    print_scores(C36_R, writer)

    C37_R = {'C37_R1_R': "what picture did you use to get the chassis itself? did you draw it or is there a load of blank formula 1 car photos I don't know about haha"
                           " I used a launch photo of the rs 17, removed the sponsors and color balanced the layers"
                           " thanks for the response haha I'm trying to learn how to make concepts like this so thank you!",
                'C37_R2_R': "what picture did you use to get the chassis itself? did you draw it or is there a load of blank formula 1 car photos I don't know about haha"
                           " I used a launch photo of the rs 17, removed the sponsors and color balanced the layers"
                           " I don't think I've ever heard of that. I'll have to check it out.",
                'C37_R3_R': "what picture did you use to get the chassis itself? did you draw it or is there a load of blank formula 1 car photos I don't know about haha"
                           " I used a launch photo of the rs 17, removed the sponsors and color balanced the layers"
                           " thanks!",
                'C37_R4_R': "what picture did you use to get the chassis itself? did you draw it or is there a load of blank formula 1 car photos I don't know about haha"
                           " I used a launch photo of the rs 17, removed the sponsors and color balanced the layers"
                           " did you use it?"
                }
    print_scores(C37_R, writer)

    C38_R = {'C38_R1_R': "congratulations op! since you already have gone to community college what field are you in / aiming for?"
                           " hi there and thank u. I am in the stem field. studying for a degree in it and comp sci."
                           " nice! when things become tough to remember URL is always rooting for you!",
                'C38_R2_R': "congratulations op! since you already have gone to community college what field are you in / aiming for?"
                           " hi there and thank u. I am in the stem field. studying for a degree in it and comp sci."
                           " I'm sorry to hear that. I hope you have a great day!",
                'C38_R3_R': "congratulations op! since you already have gone to community college what field are you in / aiming for?"
                           " hi there and thank u. I am in the stem field. studying for a degree in it and comp sci."
                           " what are you studying?",
                'C38_R4_R': "congratulations op! since you already have gone to community college what field are you in / aiming for?"
                           " hi there and thank u. I am in the stem field. studying for a degree in it and comp sci."
                           " what field?"
                }
    print_scores(C38_R, writer)

    C39_R = {'C39_R1_R': "DVD released?"
                           " not till Oct 17th digital release is tomorrow"
                           " thanks! I'll check it out. thanks!",
                'C39_R2_R': "DVD released?"
                           " not till Oct 17th digital release is tomorrow"
                           " what is this 'digital release'?",
                'C39_R3_R': "DVD released?"
                           " not till Oct 17th digital release is tomorrow"
                           " that is not how it works.",
                'C39_R4_R': "DVD released?"
                           " not till Oct 17th digital release is tomorrow"
                           " I thought it was released?"
                }
    print_scores(C39_R, writer)

    C40_R = {'C40_R1_R': "today 25th march is Tolkien reading day"
                           " unbeknownst to me, I finished watching the return of the king today at 1 am."
                           " URL: wasn't aware you were watching it?",
                'C40_R2_R': "today 25th march is Tolkien reading day"
                           " unbeknownst to me, I finished watching the return of the king today at 1 am."
                           " I have not read it yet. I'll check it out. thanks!",
                'C40_R3_R': "today 25th march is Tolkien reading day"
                           " unbeknownst to me, I finished watching the return of the king today at 1 am."
                           " same here. I loved it.",
                'C40_R4_R': "today 25th march is Tolkien reading day"
                           " unbeknownst to me, I finished watching the return of the king today at 1 am."
                           " I've been meaning to watch it for a while, but I have not seen it yet."
                }
    print_scores(C40_R, writer)

    C41_R = {'C41_R1_R': "what do you think of bill nye 's new show on Netflix?"
                           " it's terrible. I only watched the first episode though, but it was terrible."
                           " I tried to like it, but it was so cringe-worthy at parts like he was trying too hard to appeal to a young audience.",
                'C41_R2_R': "what do you think of bill nye 's new show on Netflix?"
                           " it's terrible. I only watched the first episode though, but it was terrible."
                           " I'm not sure if you 're being sarcastic or not.",
                'C41_R3_R': "what do you think of bill nye 's new show on Netflix?"
                           " it's terrible. I only watched the first episode though, but it was terrible."
                           " I liked it better than the first one.",
                'C41_R4_R': "what do you think of bill nye 's new show on Netflix?"
                           " it's terrible. I only watched the first episode though, but it was terrible."
                           " I thought it was supposed to be the first season."
                }
    print_scores(C41_R, writer)

    C42_R = {'C42_R1_R': "I really like the white shoe with a black sole, I think it 's maybe the Gel Lyte iii 'yin yang'"
                           " that's a pretty dope colorway. I have a pair of the Gel Lyte iii 's myself, they 're incredibly comfortable and super versatile"
                           " awesome dude, what CW do you have?",
                'C42_R2_R': "I really like the white shoe with a black sole, I think it 's maybe the Gel Lyte iii 'yin yang'"
                           " that's a pretty dope colorway. I have a pair of the Gel Lyte iii 's myself, they 're incredibly comfortable and super versatile"
                           " I think it's a bit of a stretch, but I don't think I've ever seen a pair of shoes in my life.",
                'C42_R3_R': "I really like the white shoe with a black sole, I think it 's maybe the Gel Lyte iii 'yin yang'"
                           " that's a pretty dope colorway. I have a pair of the Gel Lyte iii 's myself, they 're incredibly comfortable and super versatile"
                           " thanks! I'll look into it!",
                'C42_R4_R': "I really like the white shoe with a black sole, I think it 's maybe the Gel Lyte iii 'yin yang'"
                           " that's a pretty dope colorway. I have a pair of the Gel Lyte iii 's myself, they 're incredibly comfortable and super versatile"
                           " do you have a link?"
                }
    print_scores(C42_R, writer)

    C43_R = {'C43_R1_R': "absolutely. he at first agreed to let Russia question former us ambassadors and others. URL:"
                           " he would be impeached soon after he handed over those troops."
                           " he would not be impeached.",
                'C43_R2_R': "absolutely. he at first agreed to let Russia question former us ambassadors and others. URL:"
                           " he would be impeached soon after he handed over those troops."
                           " that is not how impeachment works.",
                'C43_R3_R': "absolutely. he at first agreed to let Russia question former us ambassadors and others. URL:"
                           " he would be impeached soon after he handed over those troops."
                           " that is not what he said.",
                'C43_R4_R': "absolutely. he at first agreed to let Russia question former us ambassadors and others. URL:"
                           " he would be impeached soon after he handed over those troops."
                           " your faith in republican congress may be misplaced. you did not see the Nunes story?"
                }
    print_scores(C43_R, writer)

    C44_R = {'C44_R1_R': "humans built a space rocket with stuff we found in the dirt."
                           " humans built almost everything with things we found in the dirt."
                           " I thought we were talking about the dirt.",
                'C44_R2_R': "humans built a space rocket with stuff we found in the dirt."
                           " humans built almost everything with things we found in the dirt."
                           " we are all humans on this blessed day.",
                'C44_R3_R': "humans built a space rocket with stuff we found in the dirt."
                           " humans built almost everything with things we found in the dirt."
                           " I'm not sure what you are trying to say here.",
                'C44_R4_R': "humans built a space rocket with stuff we found in the dirt."
                           " humans built almost everything with things we found in the dirt."
                           " I made pasta today with stuff found in the water."
                }
    print_scores(C44_R, writer)

    C45_R = {'C45_R1_R': "I don't remember that scene . was that in part 1/2? I just watched it."
                           " it is the opening sequence of episode 3. long surreal section taking place somewhere between the black lodge and non - existence."
                           " episode 3 is already out?",
                'C45_R2_R': "I don't remember that scene . was that in part 1/2? I just watched it."
                           " it is the opening sequence of episode 3. long surreal section taking place somewhere between the black lodge and non - existence."
                           " ah, I see. thanks for the heads up!",
                'C45_R3_R': "I don't remember that scene . was that in part 1/2? I just watched it."
                           " it is the opening sequence of episode 3. long surreal section taking place somewhere between the black lodge and non - existence."
                           " I thought it was the black mirror episode.",
                'C45_R4_R': "I don't remember that scene . was that in part 1/2? I just watched it."
                           " it is the opening sequence of episode 3. long surreal section taking place somewhere between the black lodge and non - existence."
                           " ah, I see. thanks."
                }
    print_scores(C45_R, writer)

    C46_R = {'C46_R1_R': "what is your favorite band?"
                           " led zeppelin, Greenday, Coldplay, one republic"
                           " Hello my new friend.",
                'C46_R2_R': "what is your favorite band?"
                           " led zeppelin, Greenday, Coldplay, one republic"
                           " I have never heard of this one. what is it about?",
                'C46_R3_R': "what is your favorite band?"
                           " led zeppelin, Greenday, Coldplay, one republic"
                           " I have never heard of them. I will check them out.",
                'C46_R4_R': "what is your favorite band?"
                           " led zeppelin, Greenday, Coldplay, one republic"
                           " led zeppelin?"
                }
    print_scores(C46_R, writer)

    C47_R = {'C47_R1_R': "still, she should speak English because it is an English country."
                           " wales is, by definition, the part of England & Wales that is not English."
                           " Welsh people are certainly English.",
                'C47_R2_R': "still, she should speak English because it is an English country."
                           " wales is, by definition, the part of England & Wales that is not English."
                           " no, it is not. it is a British thing.",
                'C47_R3_R': "still, she should speak English because it is an English country."
                           " wales is, by definition, the part of England & Wales that is not English."
                           " Wales isn't a country.",
                'C47_R4_R': "still, she should speak English because it is an English country."
                           " wales is, by definition, the part of England & Wales that is not English."
                           " it is not a part of the English language, it is the UK."
                }
    print_scores(C47_R, writer)

    C48_R = {'C48_R1_R': "do these come with the white laces as a spare? I see everyone posting with the white lace swap"
                           " nope I bought the laces off of rope lace supply"
                           " what laces are you talking about?",
                'C48_R2_R': "do these come with the white laces as a spare? I see everyone posting with the white lace swap"
                           " nope I bought the laces off of rope lace supply"
                           " where did you get them?",
                'C48_R3_R': "do these come with the white laces as a spare? I see everyone posting with the white lace swap"
                           " nope I bought the laces off of rope lace supply"
                           " thanks! I'll check it out! thanks!",
                'C48_R4_R': "do these come with the white laces as a spare? I see everyone posting with the white lace swap"
                           " nope I bought the laces off of rope lace supply"
                           " ok dope thanks. I think the white boosted stripes would look really clean on this color way too."
                }
    print_scores(C48_R, writer)

    C49_R = {'C49_R1_R': "tons of stuff including Shawshank. the mist. die hard 2. tales from the crypt: demon knight. he 's a great character actor."
                           " oh yeah, that guy. he looks so different as death."
                           " he also plays the British father at the end of the bogus journey ( says 'my word!' as the wyld stallyns play )",
                'C49_R2_R': "tons of stuff including Shawshank. the mist. die hard 2. tales from the crypt: demon knight. he 's a great character actor."
                           " oh yeah, that guy. he looks so different as death."
                           " I don't think I've ever seen that movie.",
                'C49_R3_R': "tons of stuff including Shawshank. the mist. die hard 2. tales from the crypt: demon knight. he 's a great character actor."
                           " oh yeah, that guy. he looks so different as death."
                           " I think he was the only one who died.",
                'C49_R4_R': "tons of stuff including Shawshank. the mist. die hard 2. tales from the crypt: demon knight. he 's a great character actor."
                           " oh yeah, that guy. he looks so different as death."
                           " he looks like he is in the movie."
                }
    print_scores(C49_R, writer)

    C50_R = {'C50_R1_R': "lpt: settle your scores irl and outside. parking lots are a good solution; you 'll get more oxygen and this tangibly improves the taste of victory."
                           " from how far up should I drop my opponent?"
                           " depends on where you live.",
                'C50_R2_R': "lpt: settle your scores irl and outside. parking lots are a good solution; you 'll get more oxygen and this tangibly improves the taste of victory."
                           " from how far up should I drop my opponent?"
                           " depends on what you're doing.",
                'C50_R3_R': "lpt: settle your scores irl and outside. parking lots are a good solution; you 'll get more oxygen and this tangibly improves the taste of victory."
                           " from how far up should I drop my opponent?"
                           " I don't get it.",
                'C50_R4_R': "lpt: settle your scores irl and outside. parking lots are a good solution; you 'll get more oxygen and this tangibly improves the taste of victory."
                           " from how far up should I drop my opponent?"
                           " as high up as you feel comfortable. first time droppers can still get noticeable results from as low as 6 inches"
                }
    print_scores(C50_R, writer)

if __name__ == '__main__':
        main()

