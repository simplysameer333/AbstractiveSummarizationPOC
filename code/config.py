base_path = '../data/'
path = base_path + 'sample_5k\\'
#path = base_path + 'stories\\'
articles_pickle_filename = "articles.pickle"
headlines_pickle_filename = "headlines.pickle"
# articles_pickle_filename = "articles_full.pickle"
# headlines_pickle_filename = "headlines_full.pickle"
vocab_to_int_pickle_filename = "vocab_to_int.pickle"
int_to_vocab_pickle_filename = "int_to_vocab.pickle"

''' https://fasttext.cc/docs/en/english-vectors.html 
    or https://www.kaggle.com/yesbutwhatdoesitmean/wikinews300d1mvec'''
model_path = '../model/'
model_org_filename = 'wiki-news-300d-1M.vec'
model_pickle_filename = "model.pickle"
word_embedding_matrix_filename = "word_embedding_matrix.pickle"
checkpoint = "./../out/best_model.ckpt"
tensorboard_logs = '../logs'

# to avoid words that are used less that threshold value
threshold = 2
enable_gpu = False

# Dimension size as per pre-trained data
embedding_dim = 300
max_text_length = 500
max_summary_length = 20
min_length = 5
unk_text_limit = 100

# Set the Hyperparameters
epochs = 100
batch_size = 10
rnn_size = 256
num_layers = 5
learning_rate = 0.002
keep_probability = 0.75
beam_width = 3

# Training Hyperparameters
start = 0
end = 4000
learning_rate_decay = 0.95
min_learning_rate = 0.0002
display_step = 10  # Check training loss after every 10 batches
stop_early = 0
stop = 3  # If the update loss does not decrease in 3 consecutive update checks, stop training
per_epoch = 3  # Make 3 update checks per epoch
