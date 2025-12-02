// Autor: DLWG

import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/#/';
const TODO_INPUT_SELECTOR = '.new-todo';

async function addTodo(page: Page, text: string) {
    await page.locator(TODO_INPUT_SELECTOR).fill(text);
    await page.keyboard.press('Enter');
}

test.describe.serial('ToDo Test - Aufgabe 4', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto(TODO_URL);
        // Alle bestehenden Todos löschen, auch bei verzögertem Entfernen
        while (await page.locator('.todo-list li').count() > 0) {
            const todoCount = await page.locator('.todo-list li').count();
            for (let i = 0; i < todoCount; i++) {
                const todo = page.locator('.todo-list li').nth(0);
                await todo.hover();
                await todo.locator('.destroy').click({ force: true });
                await expect(todo).toBeHidden();
            }
        }
    });

    test('Leere Eingabe (Enter ohne Text) erzeugt kein Todo', async ({ page }) => {
        await page.locator(TODO_INPUT_SELECTOR).focus();
        await page.keyboard.press('Enter');
        const todoCount = await page.locator('.todo-list li').count();
        expect(todoCount).toBe(0);
    });

    test('Sehr langer Text wird als Todo hinzugefügt', async ({ page }) => {
        const longText = 'a'.repeat(1000);
        await addTodo(page, longText);
        const todo = page.locator('.todo-list li label');
        await expect(todo).toHaveText(longText);
    });

    test('Verhalten ohne Todos: "Clear completed" nicht sichtbar', async ({ page }) => {
        const clearCompleted = page.locator('.clear-completed');
        await expect(clearCompleted).toBeHidden();
    });
});