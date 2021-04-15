------------
Current personachat expectation
------------

{
"train" : 
[   {   'personality': [   'I am inventive curious'],
        'utterances': [   {   'candidates': [   "something that bot should not say here",
                                                "also some nonsense that should not be relevant!",
                                                "last line that bot should use as answer'],
                              'history': ['Some history line', 'some other history line'],
                               } 
                            ]
    },
 ],
"valid" : 
[   {   'personality': [   'I am inventive curious'],
        'utterances': [   {   'candidates': [   "something that bot should not say here",
                                                "also some nonsense that should not be relevant!",
                                                "last line that bot should use as answer'],
                              'history': ['Some history line', 'some other history line'],
                               } 
                            ]
    },
 ]
}


------------
Friends proposed format
------------

'Speaker1' - Is the main character the dataset is about.

{
"train" : 
[   {   'utterances': [   {   'candidates': [   "something that bot should not say here",
                                                "also some nonsense that should not be relevant!",
                                                "last line that bot should use as answer'],
                              'history': ['Some history line', 'some other history line'],
                              'history_speakers': ['Speaker1', 'Speaker2', 'Speaker3']
                               } 
                            ]
    },
 ],
"valid" : 
[   {   'utterances': [   {   'candidates': [   "something that bot should not say here",
                                                "also some nonsense that should not be relevant!",
                                                "last line that bot should use as answer'],
                              'history': ['Some history line', 'some other history line'],
                              'history_speakers': ['Speaker1', 'Speaker2', 'Speaker3']
                               } 
                            ]
    },
 ]
}




