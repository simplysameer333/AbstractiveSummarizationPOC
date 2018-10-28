import pickle

import config
import data_processing as dp
import numpy as np
import tensorflow as tf


# This import is required becasue of tensorflow bug
# from tensorflow.contrib.seq2seq.python.ops import beam_search_ops
def text_to_cleanedup(text, vocab_to_int):
    '''Cleanup text before passing it to inference_stage'''
    text = dp.clean_text(text.split('\n'))
    text = ''.join(text)
    test_vocab_to_int = list()
    for word in text.split():
        test_vocab_to_int.append(vocab_to_int.get(word, vocab_to_int['<UNK>']))
    return test_vocab_to_int


def inference_stage(input_cleaned_test):
    checkpoint = config.checkpoint

    loaded_graph = tf.Graph()
    session_config = tf.ConfigProto(device_count={'GPU': 0})
    if config.enable_gpu:
        session_config = tf.ConfigProto(device_count={'GPU': 1})
        session_config.gpu_options.allocator_type = 'BFC'
        session_config.gpu_options.allow_growth = True

    with tf.Session(graph=loaded_graph, config=session_config) as sess:
        # Load saved model
        loader = tf.train.import_meta_graph(checkpoint + '.meta')
        loader.restore(sess, checkpoint)

        # input placeholder
        input_data = loaded_graph.get_tensor_by_name('input_data:0')
        # inference_logits define in build_graph
        logits = loaded_graph.get_tensor_by_name('predictions:0')
        # article_length placeholder
        article_length = loaded_graph.get_tensor_by_name('article_length:0')
        # headline_length placeholder
        headline_length = loaded_graph.get_tensor_by_name('headline_length:0')
        # keep_prob placeholder
        keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')

        # Multiply by batch_size to match the model's input parameters
        generated_logits = sess.run(logits, {input_data: [input_cleaned_test] * config.batch_size,
                                             headline_length: [10],
                                             article_length: [len(input_cleaned_test)] * config.batch_size,
                                             keep_prob: 1.0})[0]

    return generated_logits[0]


def main():
    print('Loading pickle for int_to_vocab ')
    ''' Loading vocab_to_int & int_to_vocab persisted during vectorization '''
    with open(config.base_path + config.vocab_to_int_pickle_filename, 'rb') as handle:
        vocab_to_int = pickle.load(handle)

    with open(config.base_path + config.int_to_vocab_pickle_filename, 'rb') as handle:
        int_to_vocab = pickle.load(handle)

    # input_text = ""
    # cleaned_text = text_to_cleanedup(input_text, vocab_to_int)

    print('Loading article data for input  ')
    with open(config.base_path + config.articles_pickle_filename, 'rb') as handle:
        clean_articles = pickle.load(handle)

    with open(config.base_path + config.headlines_pickle_filename, 'rb') as handle:
        clean_headlines = pickle.load(handle)

    random = np.random.randint(config.start, config.end)
    print('Randon index picked ', random)

    input_sentence = clean_articles[random]
    orignal_headline = clean_headlines[random]

    cleaned_text = text_to_cleanedup(input_sentence, vocab_to_int)
    generated_logits = inference_stage(cleaned_text)

    # Remove padding flag from the text
    pad = vocab_to_int["<PAD>"]

    print('Original Text: ', input_sentence)
    print('Original Headline: ', orignal_headline)
    print('Text info ')
    print('Word Ints:    {} '.format([i for i in cleaned_text]))
    print('Input Clean Words: {} '.format(" ".join([int_to_vocab[i] for i in cleaned_text])))

    print('Generated Summary')
    print("generated_logits  ", generated_logits)
    print('Word Ints:       {} '.format([i for i in generated_logits if i != pad]))
    print('Generated Words: {} '.format(" ".join([int_to_vocab[i] for i in generated_logits if i != pad])))


'''-------------------------main------------------------------'''
main()
