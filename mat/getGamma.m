function [ gamma ] = getGamma( St, Sr, Hu, Hd )

    [k, ~] = size(Hd);
    for i = 1: k
        gamma(i) = real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr));
    end

end

