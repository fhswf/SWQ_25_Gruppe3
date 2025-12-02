import { expect, test } from '@playwright/test';

test.describe('GruppeA_Aufg4 Edge Cases', () => {
    const baseUrl = 'https://demo.playwright.dev/todomvc/#/';

    test.beforeEach(async ({ page }) => {
        await page.goto(baseUrl);
        // Alle bestehenden Todos löschen, auch bei verzögertem Entfernen
        // Wiederhole, bis keine Todos mehr vorhanden sind
        while (await page.locator('.todo-list li').count() > 0) {
            const todoCount = await page.locator('.todo-list li').count();
            for (let i = 0; i < todoCount; i++) {
                const todo = page.locator('.todo-list li').nth(0);
                // .destroy-Button per Hover sichtbar machen und klicken
                await todo.hover();
                await todo.locator('.destroy').click({ force: true });
                // Warte, bis das Element entfernt wurde
                await expect(todo).toBeHidden();
            }
        }
    });

    test('Leere Eingabe (Enter ohne Text) erzeugt kein Todo', async ({ page }) => {
        await page.locator('.new-todo').focus();
        await page.keyboard.press('Enter');
        const todoCount = await page.locator('.todo-list li').count();
        expect(todoCount).toBe(0);
    });

    test('Sehr langer Text wird als Todo hinzugefügt', async ({ page }) => {
        const longText = 'a'.repeat(1000);
        await page.locator('.new-todo').fill(longText);
        await page.keyboard.press('Enter');
        const todo = page.locator('.todo-list li label');
        await expect(todo).toHaveText(longText);
    });

    test('Verhalten ohne Todos: "Clear completed" nicht sichtbar', async ({ page }) => {
        const clearCompleted = page.locator('.clear-completed');
        await expect(clearCompleted).toBeHidden();
    });
});