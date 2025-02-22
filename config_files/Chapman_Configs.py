class Config(object):
    def __init__(self,):
        self.RANDOM_SEED = 42

        # data loading para specific, do not change
        self.S_OVERLAPPING = 0.0
        self.S_TIMESTAMPS = 300

        # pretrain configs
        self.dataset = 'Chapman'
        self.input_dims = 12
        self.output_dims = 320
        self.pretrain_lr = 1e-4
        self.depth = 10
        self.pretrain_batch_size = 256
        self.shuffle_function = 'trial'  # do trial, batch or random shuffle
        self.verbose = True
        self.flag_use_multi_gpu = False
        self.n_epochs = 100
        self.masks = ['all_true', 'all_true', 'continuous', 'continuous']  # patient, trial, sample, observation
        # self.factors = [0.25, 0.25, 0.35, 0.15]  # patient, trial, sample, observation
        # self.factors = [1., 0, 0, 0]
        self.factors = [0.25] * 4

        # model and logging saved directory
        self.working_directory = 'test_run/models/' + self.dataset + '/' + '_'.join([str(factor) for factor in self.factors]) + '/'
        self.logging_directory = 'test_run/logs/' + self.dataset + '/' + '_'.join([str(factor) for factor in self.factors]) + '/'

        # finetune configs
        self.num_classes = 4

        # 100% label
        self.fraction_100 = 1.0
        self.finetune_batch_size_100 = 256
        self.finetune_epochs_100 = 50
        self.finetune_lr_100 = 1e-4

        # 10% label
        self.fraction_10 = 0.1
        self.finetune_batch_size_10 = 256
        self.finetune_epochs_10 = 50
        self.finetune_lr_10 = 1e-4

        # 1% label
        self.fraction_1 = 0.01
        self.finetune_batch_size_1 = 256
        self.finetune_epochs_1 = 50
        self.finetune_lr_1 = 1e-4


