function [ t, th] = fairFindTHD(Sr, St, Hu, Hd, Hsi)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
%        [~,k] = size(gamma);
    [k, ~] = size(Hu);
    gamma = zeros(1,k);
    for i = 1 : k
        gamma(i) = real(trace((Hd(i,:) * St * Hd(i,:)'))) * real(trace(Hu(i,:) * Sr * Hu(i,:)'));
    end
	RMax = 20;
    RMin = 0;
    
    lambs = zeros(size(gamma));
    zs = zeros(size(gamma));
    
    while (RMax - RMin > 0.005)
        R = (RMax + RMin) / 2;
		lambMax = 1000;
		lambMin = 0;
		while(lambMax - lambMin > 0.005)
			lamb = (lambMax + lambMin) / 2;
			lambs(1) = lamb;
			
			zMax = 10000;
			zMin = 0;

			while(zMax - zMin > 0.005)
				z = (zMax + zMin) / 2;
				if(lamb * (log(1 + z) - z / (1 + z)) > 1)
					zMax = z;
				else
					zMin = z;
				end
			end
			zs(1) = z;
			flag = 0;
			for i = 2: k
				gain = gamma(1) * log(1 + zs(1)) / gamma(i) / zs(1);
				if(gain >= 1)
					flag = 1;
					break;
				end
				zMax = 10000;
				zMin = 0;
				while(zMax - zMin > 0.005)
					z = (zMax + zMin) / 2;
					if(log(1 + z) < gain * z)
						zMax = z;
					else
						zMin = z;
					end
				end
				zs(i) = z;
			   	lambs(i) = 1 / (log(1 + zs(i)) - zs(i) / (1 + zs(i)));
			end

			if(flag == 1)
				lambMax = lamb;
				continue;
			end
			if(sum(lambs.*gamma./(1 + zs)) > 1)
                lambMax = lamb;
            else
                lambMin = lamb;
            end
		end
        if(sum(lambs) * R > 1)
			RMax = R;
		else
			RMin = R;
		end
    end
	t = ones(1, k + 1);
	th = zeros(1, k);
	base = 1;
	for i = 1 : k
		base = base + gamma(i) / zs(i);
	end
	t(1) = 1 / base;
	for i = 2 : k + 1
		t(i) = t(1) * gamma(i - 1) / zs(i - 1);
	   	th(i-1) = 	t(i) * log( 1 + gamma(i - 1) * t(1) / t(i));
    end
    
end

