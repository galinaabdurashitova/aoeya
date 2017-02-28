from nltk.corpus import wordnet as wn

plant = wn.synsets('plant')
plant_factory = plant[0]
plant_live = plant[1]
plant_secret = plant[3]
# использую другое слово, так как для plant растение не найдены контексты

def finding_definition(context, lemma):
    context = context.split(' ')
    context = [wn.synsets(i) for i in context]
    definition_words = lemma.definition().split(' ')
    definition_words = [wn.synsets(i) for i in definition_words]
    i = 0
    for word1 in definition_words:
        for word2 in context:
            for word in word1:
                if word in word2:
                    i += 1
                    break
    return i

print('Example: ', plant_factory.examples()[0], '\r\nDefinition:',plant_factory.definition(), '\r\nScore: ',
      finding_definition(plant_factory.examples()[0], plant_factory))
print('Example: ', plant_factory.examples()[0], '\r\nDefinition:',plant_secret.definition(), '\r\nScore: ',
      finding_definition(plant_factory.examples()[0], plant_secret))

print('Example: ', plant_secret.examples()[0], '\r\nDefinition:',plant_secret.definition(), '\r\nScore: ',
      finding_definition(plant_secret.examples()[0], plant_secret))
print('Example: ', plant_secret.examples()[0], '\r\nDefinition:',plant_factory.definition(), '\r\nScore: ',
      finding_definition(plant_secret.examples()[0], plant_factory))


hyp_plant_factory = plant_factory.hypernyms()
hyp_plant_live = plant_live.hypernyms()