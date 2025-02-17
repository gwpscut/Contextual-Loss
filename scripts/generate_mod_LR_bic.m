function generate_mod_LR_bic()

%% set parameters
% comment the unnecessary line
input_path = '/media/sdc/wpguan/BasicSR_datasets/RNI15_blur_0.5_10';
% save_mod_path = '/media/sdc/wlzhang/BasicSR/data/val/PIRMtestHR_mod';
save_LR_path = '/media/sdc/wpguan/BasicSR_datasets/RNI15_blur_0.5_10_bicX4';
%save_bic_path = '/media/sdc/wpguan/BasicSR_datasets/val_set5/Set5_blur_0.5_10_bicX4';

up_scale = 4;
mod_scale = 4;

if exist('save_mod_path', 'var')
    if exist(save_mod_path, 'dir')
        disp(['It will cover ', save_mod_path]);
    else
        mkdir(save_mod_path);
    end
end
if exist('save_LR_path', 'var')
    if exist(save_LR_path, 'dir')
        disp(['It will cover ', save_LR_path]);
    else
        mkdir(save_LR_path);
    end
end
if exist('save_bic_path', 'var')
    if exist(save_bic_path, 'dir')
        disp(['It will cover ', save_bic_path]);
    else
        mkdir(save_bic_path);
    end
end

idx = 0;
filepaths = dir(fullfile(input_path,'*.*'));
for i = 1 : length(filepaths)
    [paths,imname,ext] = fileparts(filepaths(i).name);
    if isempty(imname)
        disp('Ignore . folder.');
    elseif strcmp(imname, '.')
        disp('Ignore .. folder.');
    else
        idx = idx + 1;
        str_rlt = sprintf('%d\t%s.\n', idx, imname);
        fprintf(str_rlt);
        % read image
        img = imread(fullfile(input_path, [imname, ext]));
        % modcrop
        img = modcrop(img, mod_scale);
        if exist('save_mod_path', 'var')
            imwrite(img, fullfile(save_mod_path, [imname, '.png']));
        end
        % LR
        im_LR = imresize(img, 1/up_scale, 'bicubic');
        if exist('save_LR_path', 'var')
            imwrite(im_LR, fullfile(save_LR_path, [imname, '.png']));
        end
        %         im_B = double(im_B)/255;
        %         im_B = rgb2ycbcr(im_B);
        %         im_B = im_B(:,:,1);
        % Bicubic
        if exist('save_bic_path', 'var')
            im_B = imresize(im_LR, up_scale, 'bicubic');
            imwrite(im_B, fullfile(save_bic_path, [imname, '.png']));
        end
    end
end
end

%% modcrop
function imgs = modcrop(imgs, modulo)
if size(imgs,3)==1
    sz = size(imgs);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2));
else
    tmpsz = size(imgs);
    sz = tmpsz(1:2);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2),:);
end
end
