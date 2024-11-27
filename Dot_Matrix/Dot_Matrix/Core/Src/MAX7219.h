/*
 * MAX7219.h
 *
 *  Created on: 16 Jan 2023
 *      Author: EDISON NGUNJIRI
 */

#ifndef MAX7219_H_
#define MAX7219_H_
void Print_Alphabet(void);
void MAX7219_Init(void);
void MAX72_Init_F(void);
void Print_Dot(uint8_t row, uint8_t col);
void Set_Dot(uint8_t row, uint8_t col);
void Clear_Dot(uint8_t row, uint8_t col);
void Update_Matrix();
void Clear_Matrix();
#endif /* MAX7219_H_ */
