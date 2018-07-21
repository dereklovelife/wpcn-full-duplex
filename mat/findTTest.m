function [t,th] = findTTest(gamma)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

    %% 半双工时间分配 
    [~, k] = size(gamma);
%     gamma = zeros(1,k);
%     for i = 1 : k
%         gamma(i) = real(trace((Hd(i,:) * St * Hd(i,:)'))) * real(trace(Hu(i,:) * Sr * Hu(i,:)'));
%     end
    
    t = zeros(size(gamma) + [0, 1]);
    z_max = 100000.0;
    z_min = 0;
    gamma_sum = sum(gamma);
    time_left = 1;
    while(z_max - z_min >= 0.0001)
        z = (z_max + z_min) / 2;
        if((1 + z) * log(1 + z) - z > gamma_sum)
            z_max = z;
        else
            z_min = z;
        end
    end
    th = log(1 + z) - z / (1 + z);
    t = 0; %% 先不返回t
%     tmp = size(t);
%     tmp = tmp(2);
%     t(1) = 1 / (1 + sum(gamma) / z);
%     for i = 2 : tmp 
%         t(i) = t(1) * (gamma(i - 1) / z);
%     end
    
    
end

