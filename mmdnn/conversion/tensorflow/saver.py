import tensorflow as tf


def save_model(MainModel, network_filepath, weight_filepath, dump_filepath):
    input, model = MainModel.KitModel(weight_filepath)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

            builder = tf.saved_model.builder.SavedModelBuilder(path)

            tensor_info_input = tf.saved_model.utils.build_tensor_info(input)
            tensor_info_output = tf.saved_model.utils.build_tensor_info(model)

            prediction_signature = (
                tf.saved_model.signature_def_utils.build_signature_def(
                    inputs={'input': tensor_info_input},
                    outputs={'output': tensor_info_output},
                    method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME
                )
            )

            builder.add_meta_graph_and_variables(
                sess,
                [tf.saved_model.tag_constants.TRAINING],
                signature_def_map={
                    tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: prediction_signature
                }
            )

            save_path = builder.save()

        print('Tensorflow file is saved as [{}], generated by [{}.py] and [{}].'.format(
            save_path, network_filepath, weight_filepath))
