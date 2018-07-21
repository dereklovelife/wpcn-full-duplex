function [t, th] = newFindTTest(gamma)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
    %% 全双工时间分配
    [~, k] = size(gamma);
%     gamma = zeros(1,k);
%     for i = 1 : k
%         gamma(i) = real(trace((Hd(i,:) * St * Hd(i,:)'))) * real(trace(Hu(i,:) * Sr * Hu(i,:)'));
%     end
    
    t = zeros(size(gamma) + [0, 1]);
    
    t = zeros(size(gamma) + [0, 1]);
    zz = zeros(size(gamma));
    lamb_max = 1000;
    lamb_min = 0;
    while lamb_max - lamb_min > 0.0005
        lamb = (lamb_max + lamb_min) / 2;
        z_max = 10000;
        z_min = 0;
        while z_max - z_min > 0.005
        	z = (z_max + z_min) / 2;
			if(log(1 + z) - z /(1 + z) > lamb)
				z_max = z;
			else
				z_min = z;
			end
        end
		zz(k) = z;
        for i = k-1:-1:1
			z_max = 10000;
			z_min = 0;
			while z_max - z_min > 0.005
				z = (z_max + z_min) / 2;
				if log(1 + z) - z /(1 + z) + sum(gamma(i+1:k)./(1 + zz(i+1:k))) > lamb
					z_max = z;
				else
					z_min = z;
				end
			end
			zz(i) = z;
        end
		if sum(gamma./(1 + zz)) > lamb
			lamb_min = lamb;
		else
			lamb_max = lamb;
        end
        
    end
    
    lamb
	time_left = 1;
	i = k + 1;
    while(i > 1)
        i = i - 1;
        t(i+1) = time_left / (1 + zz(i) / gamma(i));
        time_left = time_left - t(i+1);
    end
    t(1) = time_left;
    th = 0;
    tmp = size(t);
    tmp = tmp(2);
    for i = 1: tmp - 1
        th = th + t(i + 1) * log(1 + gamma(i) * sum(t(1:i)) / t(i + 1));
    end
    zz  
end

