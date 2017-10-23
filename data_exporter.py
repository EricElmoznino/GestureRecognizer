import os
import scipy.io
import zipfile
import re

def load_sample(filepath, sample_id):
    mat = scipy.io.loadmat(filepath,struct_as_record=False)['Video'][0][0]

    frame_filepath = os.path.join('processed_data', 'joints_'+str(sample_id)+'.txt')
    label_filepath = os.path.join('processed_data', 'labels_'+str(sample_id)+'.txt')

    frames = mat.Frames[0]
    with open(frame_filepath, 'w') as f:
        for frame in frames:
            skeleton = frame.Skeleton[0][0]
            joint_positions = skeleton.WorldPosition
            joint_positions = str(joint_positions)
            joint_positions = joint_positions.replace('\n', ',')
            joint_positions = joint_positions[1:-2]
            f.write(joint_positions+'\n')

    labels = mat.Labels[0]
    with open(label_filepath, 'w') as l:
        for label in labels:
            rep = int(label.End-label.Begin)+1
            label_name=label.Name[0]
            for i in range(0,rep):
                l.write(label_name+'\n')


def load_dataset(dir):
    for sub_dir in os.listdir(dir):
        if re.match('Sample[0-9]*$', sub_dir) is None:
            continue
        sample_id = int(sub_dir.replace('Sample', ''))
        filepath = os.path.join(dir, sub_dir, sub_dir) + '_data.mat'
        load_sample(filepath, sample_id)


def unzip_file(filepath):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(filepath.replace('.zip', ''))


def unzip(dir):
    for name in os.listdir(dir):
        file = os.path.join(dir, name)
        if 'zip' not in file:
            continue
        unzip_file(file)