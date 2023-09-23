//
// Created by Ethan on 9/13/2023.
//

#include <vector>
#include <utility>
#include "action.h"

#ifndef LEARNSOMETHING_HACKATHONBOT_H
#define LEARNSOMETHING_HACKATHONBOT_H

enum DELTA_SIGN {
    POSITIVE = 1,
    NEGATIVE = -1,
    ZERO = 0
};

class HackathonBot {
public:
    HackathonBot();
    void takeAction(float price);
    double getBalance();
    bool isHolding();
private:
    double purchasePrice; // 100
    std::vector<double> prices;
    std::vector<double> delta; // derivative
    int in_a_row; // ups and downs in a row
    int current_sign; // DELTA_SIGN
    int within_five_percent;
    double balance;
    bool holding;
};

#endif //LEARNSOMETHING_HACKATHONBOT_H
