import { expect, Page, test } from '@playwright/test';

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/');
    });

    test("Ein neues Todo wird hinzugefügt", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein erstes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
    });

    // TODO: Fügen Sie hier Ihre Tests ein
    // Folgen Sie den Anleitungen in der README.md
});
