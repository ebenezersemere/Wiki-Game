
try:
    from src import *
except Exception:
    pass

try:
    from WikiGame.src import *
except Exception:
    pass



if __name__ == "__main__":
    # origin = input("Enter the origin page: ")
    # while not valid_link(origin):
    #     print("Invalid link. P®lease enter a valid Wikipedia topic.")
    #     origin = input("Enter the origin page: ")
    #
    # destination = input("Enter the destination page: ")
    # while not valid_link(destination):
    #     print("Invalid link. Please enter a valid Wikipedia topic.")
    #     destination = input("Enter the destination page: ")
    #
    # algorithm = input("Enter the algorithm: ")
    # while not (algorithm == "Greedy" or algorithm == "Backtrack"):
    #     print("Invalid algorithm. Please enter 'Greedy' or 'Backtrack'.")
    #     algorithm = input("Enter the algorithm: ")
    #
    # model = input("Enter the model: ")
    # while not (model == "WordVec"):
    #     print("Invalid model. Please enter 'WordVec'.")
    #     model = input("Enter the model: ")
    # model = WordVec()
    # l = ['A. H. Almaas', 'A. J. Ayer', 'Abdel Rahman Badawi', 'Abhinavagupta', 'Abiogenesis', 'Abraham Joshua Heschel', 'Abu al-Hassan al-Amiri', 'Accident (philosophy)', 'Acosmism', 'Adi Shankara', 'Aesthetic', 'Afrikan Spir', 'Afterlife', 'Agnosticism', 'Al-Farabi', 'Al-Ghazali', 'Al-Kindi', 'Al-Shahrastani', 'Albert Camus', 'Albrecht Ritschl', 'Alexander Pruss', 'Ali Akbar Rashad', 'Ali Shariati', 'Alister McGrath', 'Aloysius Martinich', 'Alvin Plantinga', 'Analytic-synthetic distinction', 'Analytic philosophy', 'Ancient Greek philosophy', 'Animism', 'Anselm of Canterbury', 'Anthony Kenny', 'Anthony Thiselton', 'Anthropopathism', 'Antireligion', 'Antoine Augustin Calmet', 'Antony Flew', 'Apologetics', 'Apophatic theology', 'Argument from a proper basis', 'Argument from beauty', 'Argument from consciousness', 'Argument from degree', 'Argument from desire', 'Argument from free will', 'Argument from inconsistent revelations', 'Argument from love', 'Argument from miracles', 'Argument from morality', 'Argument from nonbelief', 'Argument from poor design', 'Argument from reason', 'Argument from religious experience', 'Arthur Schopenhauer', 'Atheism', "Atheist's Wager", 'Atheistic existentialism', 'Augustine of Hippo', 'Augustinian theodicy', 'Avempace', 'Averroes', 'Avicenna', 'Ayn Rand', "Baron d'Holbach", 'Baruch Spinoza', 'Basil Mitchell (academic)', 'Belief', 'Belief-in', 'Bertrand Russell', 'Best of all possible worlds', 'Bible', 'Bimal Krishna Matilal', 'Blaise Pascal', 'Boethius', 'Brahman', 'Brethren of Purity', 'Brian Leftow', 'Buddha', 'Buddhaghosa', 'C. Stephen Evans', 'Carl Ernst', 'Cataphatic theology', 'Charles Bell', 'Charles Hartshorne', 'Charles Taliaferro', 'Christian existentialism', 'Christian humanism', 'Christological argument', 'Christology', 'Christopher Hitchens', 'Conceptions of God', 'Cosmological argument', 'Creation myth', 'Creationism', 'Creator in Buddhism', 'Criticism of religion', 'D. Z. Phillips', 'Damien Keown', 'Daniel Dennett', 'David Hume', 'David Loy', 'Dean Zimmerman (philosopher)', 'Deism', 'Demiurge', 'Demonology', 'Demythologisation', 'Desacralization of knowledge', 'Desiderius Erasmus', 'Dewi Zephaniah Phillips', 'Dharma', 'Dharmakirti', 'Dignāga', 'Divine command theory', 'Divine simplicity', 'Dorothy Emmet', 'Dualism in cosmology', 'Dualistic cosmology', 'Early modern philosophy', 'East Asian religions', 'Elizabeth Burns (philosopher)', 'Emil Brunner', 'Empirical evidence', 'Empiricism', 'Enlightenment (spiritual)', 'Enquiry Concerning Human Understanding', 'Epicurus', 'Equivocation', 'Ernst Cassirer', 'Ernst Haeckel', 'Ernst Troeltsch', 'Eschatological verification', 'Eschatological verificationism', 'Eschatology', 'Ethical egoism', 'Ethics in religion', 'Euthyphro dilemma', 'Evan Thompson', 'Evil God challenge', 'Exclusivism', 'Exegesis', 'Existence of God', 'Existentialism', 'Faith', 'Faith and rationality', 'Fakhr al-Din al-Razi', 'Fate of the unlearned', 'Feminist theology', 'Fideism', 'Fine-tuned universe', 'Folklore', 'Form of life', 'Form of the Good', 'Francis Schaeffer', 'Franklin I. Gamwell', 'Françoise Meltzer', 'Frederick Ferré', 'Friedrich Nietzsche', 'Friedrich Schleiermacher', 'Frithjof Schuon', 'Fundamentalism', 'Gabriel Marcel', 'Gaudapada', 'Gaunilo of Marmoutiers', 'Georg Wilhelm Friedrich Hegel', 'George Berkeley', 'George I. Mavrodes', 'George Santayana', 'Georges Tamer', 'Giovanni Pico della Mirandola', 'Gnosticism', 'God', 'God in Abrahamic religions', 'God in Christianity', 'God in Hinduism', 'God in Islam', 'God in Jainism', 'God in Judaism', 'God in Mormonism', 'God in Sikhism', "God in the Bahá'í Faith", 'God in the Baháʼí Faith', 'God of the gaps', 'Gordon Graham (philosopher)', 'Gottfried Wilhelm Leibniz', 'Guru Granth Sahib', 'Gustav Glogau', "Gödel's ontological proof", 'Hajime Nakamura', 'Harald Høffding', 'Hayyi Rabbi', 'Henotheism', 'Heraclitus', 'Herbert McCabe', 'History of religion', "Hitchens's razor", 'Holy Spirit', 'Hossein Nasr', 'Humanism', 'Humanistic naturalism', 'Huston Smith', 'ISBN (identifier)', 'ISSN (identifier)', 'Ian Ramsey', 'Ibn Arabi', 'Ibn Masarra', 'Immanuel Kant', 'Incarnation (Christianity)', 'Inclusivism', 'Incompatible-properties argument', 'Inconsistent triad', 'Index of philosophy of religion articles', 'Indiana Philosophy Ontology Project', 'Ineffability', 'Ingolf U. Dalferth', 'Intelligent design', 'Internet Encyclopedia of Philosophy', 'Irenaean theodicy', 'Ivan Esaulov', 'J. J. C. Smart', 'J. Krishnamurti', 'J. L. Austin', 'J. L. Mackie', 'James VI and I', 'Jan Westerhoff', 'Jay L. Garfield', 'Jayanta Bhatta', 'Jean-Luc Marion', 'Jean-Paul Sartre', 'Jennifer Michael Hecht', 'Jewish philosophy', 'Johann Gottfried Herder', 'John Caird (theologian)', 'John Henry Newman', 'John Hick', 'John McIntyre (theologian)', 'John Searle', 'John Stuart Mill', 'John Wisdom', 'Jonathan Kvanvig', 'Joseph B. Soloveitchik', 'Joseph Maréchal', 'Joseph Runzo', 'Junkyard tornado', 'K. N. Jayatilleke', 'Kalam cosmological argument', 'Karl Barth', 'Karl Christian Friedrich Krause', 'Karl Marx', 'Kazimierz Łyszczyński', 'Keiji Nishitani', 'Keith Ward', 'Keith Yandell', 'Kitaro Nishida', 'Klaus Klostermaier', 'Krishna Chandra Bhattacharya', 'Kumārila Bhaṭṭa', 'LIT Verlag', 'Langdon Brown Gilkey', 'Language, Truth and Logic', 'Language-games', 'Language game (philosophy)', 'Language games', 'Leap of faith', 'Lev Shestov', "Lewis's trilemma", 'List of philosophies', 'Logical positivism', 'Logical truth', 'Lotus Sutra', 'Louis Dupré (philosopher)', 'Loyal Rue', 'Lucretius', 'Ludwig Feuerbach', 'Ludwig Wittgenstein', 'Lutheranism', 'Lynn de Silva', 'Madhvacharya', 'Maimonides', 'Marcion of Sinope', 'Martin Buber', 'Martin Heidegger', 'Martin Lings', 'Mathematics and God', 'Medieval philosophy', 'Meditation', 'Meinongian argument', 'Melville Y. Stewart', 'Metaphysical naturalism', 'Metaphysics', 'Michael Lou Martin', 'Michael Zank', 'Michel Foucault', 'Mir Damad', 'Miracle', 'Mircea Eliade', 'Miskawayh', 'Misotheism', 'Molecular genetics', 'Monism', 'Monotheism', 'Moses Mendelssohn', 'Muhammad Iqbal', 'Mulla Sadra', 'Mysticism', 'Nagarjuna', 'Nathan Katz (professor)', 'Natural-law argument', 'Natural evil', 'Natural theology', 'Naturalism (philosophy)', 'New Age', 'Nicholas Wolterstorff', 'Nicolas Malebranche', 'Nondualism', 'Nontheism', 'Norman Kretzmann', 'Norman Malcolm', 'Nyayakusumanjali', "Occam's razor", 'Omnipotence paradox', 'Ontological argument', 'P. D. Premasiri', 'Pamela Sue Anderson', 'Pandeism', 'Panentheism', 'Pantheism', 'Parable', 'Parable of the Invisible Gardener', "Pascal's wager", 'Paul Draper (philosopher)', 'Paul Moser', 'Paul Tillich', 'Pavel Florensky', 'Perennial philosophy', 'Personal god', 'Peter Geach', 'Peter Singer', 'Peter Winch', 'Peter van Inwagen', 'PhilPapers', 'Phillip H. Wiebe', 'Philosophical Investigations', 'Philosophy of Baruch Spinoza', 'Philosophy of religion', 'Polytheism', 'Possibilianism', 'Problem of Hell', 'Problem of evil', 'Problem of the Creator of God', 'Process theology', 'Proof of the Truthful', 'Proslogion', 'R. B. Braithwaite', 'R. M. Hare', 'Raghunatha Siromani', 'Ramana Maharshi', 'Ramanuja', 'Ravi Zacharias', 'Rebecca Goldstein', 'Reformed epistemology', 'Reincarnation', 'Reinhold Niebuhr', 'Relationship between religion and science', 'Religion', 'Religious experience', 'Religious humanism', 'Religious naturalism', 'Religious philosophy', 'Religious pluralism', 'Religious responses to the problem of evil', 'Religious skepticism', 'Religious text', 'René Descartes', 'René Guénon', 'Resurrection', 'Resurrection of Jesus', 'Richard Dawkins', 'Richard Swinburne', 'Robert K. C. Forman', 'Robert Merrihew Adams', 'Rudolf Bultmann', 'Rudolf Otto', 'Rush Rhees', "Russell's teapot", 'Sam Harris', 'Sarvepalli Radhakrishnan', 'Secular humanism', 'Seddiqin argument', 'Seiichi Hatano', 'Sergei Bulgakov', 'Shah Waliullah Dehlawi', 'Shahab al-Din Yahya ibn Habash Suhrawardi', 'Shamanism', 'Shaykh Tusi', 'Sikhism', 'Simon Critchley', 'Simone Weil', 'Simone de Beauvoir', 'Son of God', 'Soul', 'Spiritualism (beliefs)', 'Sri Aurobindo', 'Steven Schwarzschild', 'Summum bonum', 'Supreme Being', 'Syed Muhammad Naquib al-Attas', 'Søren Kierkegaard', 'Taede A. Smedes', 'Tariq Ramadan', 'Teleological argument', 'Thealogy', 'Theism', 'Theodicy', 'Theodore Drange', 'Theological noncognitivism', 'Theological veto', 'Theology', 'Theories about religions', 'Thomas Aquinas', 'Thomas Carlyle', 'Thomas Chubb', 'Tractatus Logico-Philosophicus', 'Trademark argument', 'Transcendent theosophy', 'Transcendental argument for the existence of God', 'Transcendentalism', 'Trenton Merricks', 'Udayana', 'Ultimate Boeing 747 gambit', 'Unfalsifiable', 'Univocity', 'Unmoved mover', 'Vasubandhu', 'Verifiability theory of meaning', 'Verificationism', 'Vernon White (theologian)', 'Vienna Circle', 'Vincent Brümmer', 'Vincent Miceli', 'Vitalism', 'Vladimir Solovyov (philosopher)', 'Voltaire', 'Vācaspati Miśra', 'Walter Kaufmann (philosopher)', 'Watchmaker analogy', 'Western esotericism', 'Wiccan views of divinity', 'Willard Van Orman Quine', 'William Alston', 'William F. Vallicella', 'William James', 'William Kingdon Clifford', 'William L. Rowe', 'William Lane Craig', 'William Paley', 'William S. Hatcher', 'William Whewell', 'William Wollaston', 'William of Ockham', 'Wolfgang Smith', 'Womanist theology', 'Ñāṇavīra Thera', 'Wikipedia:Featured articles', 'Template:Philosophy of religion', 'Template:Philosophy of religion sidebar', 'Template talk:Philosophy of religion', 'Template talk:Philosophy of religion sidebar', 'Category:Christian philosophers', 'Category:Hindu philosophers and theologians', 'Category:Islamic philosophers', 'Category:Jewish philosophers', 'Category:Philosophers of religion', 'Category:Philosophy of religion', 'Category:Scholars of Buddhism', 'Portal:Philosophy']
    # print(get_closest(clean_list(l), "Religious text", 10))

    origin = "Computer science"
    destination = "Time"
    algorithm = Greedy
    #model = "WordVec"
    
    # load the model
    pickle_path = ("/Users/ebenezersemere/Workspace/Student/Pomona"
                   "/Natural Language Processing/Final Project/WikiGame/data/glove.pickle")

    pickle_path = "/Users/reneau-cardoso/projects/Wiki-Game/WikiGame/data/glove.pickle"

    with open(pickle_path, 'rb') as f:
        data = pickle.load(f)
        
    model = WordVec(data)

    game = WikiGame(origin, destination, algorithm, model)
    path = game.play_game()

    # print(is_redirect_page("The Foot of Cupid"))
    # print(find_hyperlinks("The Foot of Cupid"))
    # print(find_hyperlinks("The Foot of Cupid"))
    print(f"Path taken: {path}")

    # look at line 69 in wordvec.py
