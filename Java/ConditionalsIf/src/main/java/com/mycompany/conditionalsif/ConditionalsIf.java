/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.conditionalsif;

/**
 *
 * @author msi3
 */
public class ConditionalsIf {

    public static void main(String[] args) {
        Blackjack blackjack = new Blackjack();
        
        System.out.println(blackjack.parseCard("ace"));
        System.out.println(blackjack.isBlackjack("queen", "ace"));
        boolean isBlackJack = true;
        int dealerScore = 7;

        System.out.println(blackjack.largeHand(isBlackJack, dealerScore));
        
        int handScore = 15;
        int dealerScore2 = 12;
        System.out.println(blackjack.smallHand(handScore, dealerScore2));
    }
}
