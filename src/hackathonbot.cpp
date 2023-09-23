//
// Created by Ethan on 9/13/2023.
//

#include <iostream>

#include "hackathonbot.h"

HackathonBot::HackathonBot() : purchasePrice(100), balance(0), holding(true), in_a_row(0) {
  this->prices.push_back(100);
  this->delta.push_back(0);
  this->current_sign = ZERO; // up / down
}

void HackathonBot::takeAction(float price) {
  double mostRecentPrice = this->prices[this->prices.size() - 1];
  this->prices.push_back(price);

  double newDelta = price - mostRecentPrice;
  double mostRecentDelta = this->delta[this->delta.size() - 1];
  this->delta.push_back(newDelta);

  if((abs((price - this->purchasePrice)/this->purchasePrice)) < 0.05) {
    this->within_five_percent ++;
  } else {
    this->within_five_percent = 0;
  }

  if(newDelta == 0) {
    this->current_sign = ZERO;
    this->in_a_row = 0;
  } else if(!!(newDelta > 0 ^ mostRecentDelta < 0) || mostRecentDelta == 0) {
    this->in_a_row ++;
  } else {
    this->in_a_row = 1;
    this->current_sign = newDelta > 0 ? POSITIVE : NEGATIVE;
  }

  if(this->holding) {
    // determine if sell or not
    if((in_a_row >= 52 && current_sign == POSITIVE) || (in_a_row >= 47 && current_sign == NEGATIVE)) {
      this->holding = false;
      this->balance += price;
      return;
    }

    if(within_five_percent >= 10) {
      this->holding = false;
      this->balance += price;
      return;
    }

    if(price <= this->purchasePrice * 0.38 || price >= this->purchasePrice * 1.89) {
      this->holding = false;
      this->balance += price;
      return;
    }
  } else {
    // determine if buy or not
    if(price < 52 || (in_a_row >= 5 && current_sign == NEGATIVE)) {
      this->holding = true;
      this->purchasePrice = price;
      this->balance -= price;
      return;
    }
  }
}

double HackathonBot::getBalance() {
  return this->balance;
}

bool HackathonBot::isHolding() {
  return this->holding;
}

