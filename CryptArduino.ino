#include <EEPROM.h>

const int key = 0xA5; //hex for 165, ascii value of a special character
const int offset = 7;  //offset for translation
const int adrrkey = 11; //offset for address of encrypted code
const char* sampleCode = "4287"; //test code can be changed

void encrypt(const char* code); // Encrypt the code and store it in EEPROM
void decrypt(char* code); // Read the encrypted code from EEPROM and decrypt it
bool verifyCode(const char* code); // Call the decrypt function and compare the codes
void getCode(char* code); // Get user input code from the Serial Monitor

void setup() {
    Serial.begin(9600);
    while (!Serial) {
        ;  //wait till Serial begins ie connects
    }
    encrypt(sampleCode); //store the encrypted code once, to be read and decrypted later
}

void loop() {
    char userInput[5];
    Serial.print("Enter 4-digit access code: ");
    getCode(userInput);
    userInput[4] = '\0'; //save the code as a string
    Serial.println(userInput); //show the entered code
  
    if (verifyCode(userInput)) {
        Serial.println("Access Granted");
    } else {
        Serial.println("Access Denied");
    }
    delay(3000);
}

// Encrypt the code and store it in EEPROM
void encrypt(const char* code) {
    for (int i = 0; i < 4; i++) {
        char ench = (code[i] ^ key) + offset; //apply XOR then a simple translation
        EEPROM.write(i + adrrkey, ench); //store in an address with a given offset for additional security
    }
}

// Read the encrypted code from EEPROM and decrypt it
void decrypt(char* code) {
    for (int i = 0; i < 4; i++) {
        char ench = EEPROM.read(i + adrrkey);  //read from the offset address
        code[i] = (ench - offset) ^ key; //reverse the encryption
    }
    code[4] = '\0'; 
}

// Decrypt the encrypted code and verify the input code using this
bool verifyCode(const char* code) {
    char temp[5];
    decrypt(temp);
    return strcmp(temp, code) == 0; //strcmp is a string fucntion that sort of subtracts two strings, hence 0 is returned only when both the strings are exactly same
}

// Get user input from the Serial Monitor
void getCode(char* code) {
    int c = 0;
    while (c < 4) { //read first 4 characters
        if (Serial.available() > 0) { 
            char ch = Serial.read();
            if (ch >= '0' && ch <= '9') {
                code[c] = ch; //store entered digit as a character
                c++;
            } else {
                Serial.println("Invalid Character, ignoring the character, enter the rest of the code"); //error if a character other than a number is entered
                while (Serial.available() > 0) {
                    Serial.read(); // ignore anything entered after the character
           }}}}
    code[4] = '\0';  //save as a string
    while (Serial.available() > 0) {
        Serial.read(); //ignore anything more than 4 characters
    }
}
