import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

mq.index("my-first-index").add_documents([
    {
     'id': "1",
     'name':"The Pilgrim’s Progress",
     'description' : "A story of a man in search of truth told with the simple clarity and beauty of Bunyans prose make this the ultimate English classic.",
                       
    },
    {
      'id': "2",  
      'name': "Robinson Crusoe", 
      'description' : "By the end of the 19th century, no book in English literary history had enjoyed more editions, spin-offs and translations. Crusoe’s world-famous novel is a complex literary confection, and it’s irresistible."
    },
    {
      'id': "3",
      'name': " Gulliver’s Travels", 
      'description' : "A satirical masterpiece that’s never been out of print, Jonathan Swift’s Gulliver’s Travels comes third in our list of the best novels written in English"
    },
    {
      'id': "4",  
      'name': "Clarissa", 
      'description' : "Clarissa is a tragic heroine, pressured by her unscrupulous nouveau-riche family to marry a wealthy man she detests, in the book that Samuel Johnson described as “the first book in the world for the knowledge it displays of the human heart.”"
    },
    {
      'id': "5",  
      'name': " Tom Jones ", 
      'description' : "Tom Jones is a classic English novel that captures the spirit of its age and whose famous characters have come to represent Augustan society in all its loquacious, turbulent, comic variety."
    },
    {
      'id': "6",  
      'name': " The Life and Opinions of Tristram Shandy, Gentleman", 
      'description' : "Laurence Sterne’s vivid novel caused delight and consternation when it first appeared and has lost little of its original bite."
    },
    ]
)

results = mq.index("my-first-index").search(
    q="Man lost on an Island"
)


pprint.pprint(results)
