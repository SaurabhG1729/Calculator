#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

#define EXPORT __declspec(dllexport)

typedef struct {
    int precedence;
    bool right_assoc;
} Operator;

Operator get_op_info(char c) {
    switch (c) {
        case '+': case '-': return (Operator){2, false};
        case '*': case '/': return (Operator){3, false};
        case '^':           return (Operator){4, true};
        default:            return (Operator){0, false};
    }
}

bool is_op(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

// NEW: The Validation Algorithm
bool is_valid_infix(const char* expr) {
    int len = strlen(expr);
    bool last_was_op = true; // Acts as if we just saw an op to prevent starting with one
    bool has_digit = false;

    for (int i = 0; i < len; i++) {
        if (isspace(expr[i])) continue;

        if (isdigit(expr[i]) || expr[i] == '.') {
            last_was_op = false;
            has_digit = true;
            // Skip the rest of the number
            while (i + 1 < len && (isdigit(expr[i+1]) || expr[i+1] == '.')) i++;
        } 
        else if (is_op(expr[i])) {
            if (last_was_op) return false; // Two ops in a row or starts with op
            last_was_op = true;
        } 
        else {
            return false; // Unexpected character
        }
    }

    // Cannot end with an operator and must contain at least one digit
    return !last_was_op && has_digit;
}

double apply_op(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return (b == 0) ? NAN : a / b;
        case '^': return pow(a, b);
        default:  return 0;
    }
}

EXPORT double evaluate(const char* expression) {
    // PRE-CHECK: If invalid, return NaN immediately
    if (!is_valid_infix(expression)) return NAN;

    double val_stack[100];
    char op_stack[100];
    int v_top = -1, o_top = -1;

    for (int i = 0; expression[i] != '\0'; i++) {
        if (isspace(expression[i])) continue;

        if (isdigit(expression[i]) || expression[i] == '.') {
            char *endptr;
            val_stack[++v_top] = strtod(&expression[i], &endptr);
            i = (int)(endptr - expression) - 1;
        } 
        else if (is_op(expression[i])) {
            char cur_char = expression[i];
            Operator cur_op = get_op_info(cur_char);

            while (o_top != -1) {
                Operator top_op = get_op_info(op_stack[o_top]);
                if (top_op.precedence > cur_op.precedence ||
                   (top_op.precedence == cur_op.precedence && !cur_op.right_assoc)) {
                    
                    if (v_top < 1) return NAN; // Safety break
                    double b = val_stack[v_top--];
                    double a = val_stack[v_top--];
                    val_stack[++v_top] = apply_op(a, b, op_stack[o_top--]);
                } else break;
            }
            op_stack[++o_top] = cur_char;
        }
    }

    while (o_top != -1) {
        if (v_top < 1) return NAN;
        double b = val_stack[v_top--];
        double a = val_stack[v_top--];
        val_stack[++v_top] = apply_op(a, b, op_stack[o_top--]);
    }

    return (v_top == 0) ? val_stack[v_top] : NAN;
}