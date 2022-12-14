"""
DTO  class holding config parameters for DQN training
"""

import csv

class QHDConfig:
    """
    Configuration parameters for DQN
    """

    def __init__(self,
                 input_dim: int,
                 attacker_output_dim: int = 33,
                 defender_output_dim: int = 33,
                 replay_memory_size: int = 100000,
                 batch_size: int = 64,
                 target_network_update_freq: int = 10,
                 gpu: bool = False,
                 tensorboard : bool = False,
                 tensorboard_dir: str = "",
                 lr_exp_decay: bool = False,
                 lr_decay_rate: float = 0.96,
                 state_length = 1,
                 dimension=1000,
                 merged_ad_features: bool = False,
                 normalize_features: bool = False,
                 zero_mean_features: bool = False):
        """
        Initializes the config

        :param input_dim: input dimension of the DQN networks
        :param attacker_output_dim: output dimensions of the DQN networks for the attacker
        :param defender_output_dim: output dimensions of the DQN networks for the defender
        :param replay_memory_size: replay memory size
        :param batch_size: the batch size during training
        :param target_network_update_freq: the frequency (in episodes) of updating the target network
        :param gpu: boolean flag whether using GPU or not
        :param tensorboard: boolean flag whether using tensorboard logging or not
        :param tensorboard_dir: tensorboard logdir
        :param lr_exp_decay: whether to use exponential decay of learning rate or not
        :param lr_decay_rate: decay rate of lr
        :param state_length: length of state (Whether stacking observations or not)
        :param merged_ad_features: boolean flag inidicating whether defense and attack features should be merged
        :param normalize_features: boolean flag whether features should be normalized or not
        :param zero_mean_features: boolean flag whether features should be converted to zero-mean vectors
        """
        self.input_dim = input_dim
        self.attacker_output_dim = attacker_output_dim
        self.defender_output_dim = defender_output_dim
        self.replay_memory_size = replay_memory_size
        self.batch_size = batch_size
        self.target_network_update_freq = target_network_update_freq
        self.gpu = gpu
        self.tensorboard = tensorboard
        self.tensorboard_dir = tensorboard_dir
        self.lr_exp_decay = lr_exp_decay
        self.lr_decay_rate = lr_decay_rate
        self.state_length = state_length
        self.dimension = dimension
        self.merged_ad_features = merged_ad_features
        self.normalize_features = normalize_features
        self.zero_mean_features = zero_mean_features

    def to_str(self) -> str:
        """
        :return: a string with information about all of the parameters
        """
        return "DQN Hyperparameters: input_dim:{0},attacker_output_dim:{1}, defender_output_dim:{2}," \
                "replay_memory_size:{3}, batch_size:{4}, target_network_update_freq:{5}," \
                "gpu:{6}, tensorboard:{7}, tensorboard_dir:{8}," \
                "lr_exp_decay:{9},lr_decay_rate:{10}," \
                "state_length:{11}, dimension:{12}, merged_ad_features:{13}," \
                "normalize_features:{14}, zero_mean_features:{15}".format(
            self.input_dim, self.attacker_output_dim, self.defender_output_dim,
            self.replay_memory_size, self.batch_size, self.target_network_update_freq,
            self.gpu, self.tensorboard, self.tensorboard_dir,
            self.lr_exp_decay, self.lr_decay_rate,
            self.state_length, self.dimension, self.merged_ad_features,
            self.normalize_features, self.zero_mean_features)

    def to_csv(self, file_path: str) -> None:
        """
        Write parameters to csv file

        :param file_path: path to the file
        :return: None
        """
        with open(file_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["parameter", "value"])
            writer.writerow(["input_dim", str(self.input_dim)])
            writer.writerow(["attacker_output_dim", str(self.attacker_output_dim)])
            writer.writerow(["defender_output_dim", str(self.defender_output_dim)])
            writer.writerow(["replay_memory_size", str(self.replay_memory_size)])
            writer.writerow(["batch_size", str(self.batch_size)])
            writer.writerow(["target_network_update_freq", str(self.target_network_update_freq)])
            writer.writerow(["gpu", str(self.gpu)])
            writer.writerow(["tensorboard", str(self.tensorboard)])
            writer.writerow(["tensorboard_dir", str(self.tensorboard_dir)])
            writer.writerow(["lr_exp_decay", str(self.lr_exp_decay)])
            writer.writerow(["lr_decay_rate", str(self.lr_decay_rate)])
            writer.writerow(["state_length", str(self.state_length)])
            writer.writerow(["dimension", str(self.dimension)])
            writer.writerow(["merged_ad_features", str(self.merged_ad_features)])
            writer.writerow(["normalize_features", str(self.normalize_features)])
            writer.writerow(["zero_mean_features", str(self.zero_mean_features)])