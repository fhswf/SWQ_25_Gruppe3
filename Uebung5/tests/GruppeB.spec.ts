// Teilnehmer: RNSR und ANGE

import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/';

async function addTodo(page: Page, text: string) {
    const input = page.getByPlaceholder('What needs to be done?');
    await input.fill(text);
    await input.press('Enter');
}

test.describe('1. Grundlegend', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    //RNSR
    test("Ein Todo hinzufügen", async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');

        await expect(page.getByText('Erster Eintrag')).toBeVisible();
    });
    //ANGE
    test("mehrere Todos hinzufügen", async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');

        await expect(page.getByText('Erster Eintrag')).toBeVisible();
        await expect(page.getByText('Zweiter Eintrag')).toBeVisible();
    });
    //RNSR
    test("Checkboxen setzen", async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        const checkerbox = page.getByRole("checkbox", { name: 'Toggle Todo' })

        await page.getByRole('checkbox', { name: 'Toggle Todo' }).check();
    });
    //ANGE
    test("Zähler „items left“ prüfen", async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        const locator = page.getByRole('strong');
        await expect(locator).toHaveText("1");
    });

});

test.describe('2. Löschen & Toggle-All', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    //RNSR
    test('Todo via X löschen', async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');

        const firstItem = page.locator('.todo-list li').first();
        await firstItem.hover();

        await firstItem.locator('.destroy').click();

        await expect(page.getByText('Erster Eintrag')).toHaveCount(0);
        await expect(page.getByText('Zweiter Eintrag')).toBeVisible();
    });
    //ANGE
    test('Toggle-All setzt alle Todos auf erledigt/nicht erledigt', async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');
        await addTodo(page, 'Dritter Eintrag');

        const checks = page.locator('.todo-list li input[type="checkbox"]');
        await checks.nth(1).check();

        const toggleAll = page.locator('input.toggle-all, #toggle-all');
        await toggleAll.check();

        const count = await checks.count();
        for (let i = 0; i < count; i++) {
            await expect(checks.nth(i)).toBeChecked();
        }
        await toggleAll.uncheck();
        for (let i = 0; i < count; i++) {
            await expect(checks.nth(i)).not.toBeChecked();
        }
    });
    //RNSR
    test('„Clear completed“ entfernt erledigte', async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');
        await addTodo(page, 'Dritter Eintrag');

        const checks = page.locator('.todo-list li input[type="checkbox"]');
        await checks.nth(0).check();
        await checks.nth(1).check();

        await page.getByText('Clear completed').click();

        await expect(page.getByText('Erster Eintrag')).toHaveCount(0);
        await expect(page.getByText('Zweiter Eintrag')).toHaveCount(0);
        await expect(page.getByText('Dritter Eintrag')).toBeVisible();
    });
});

test.describe('3. Filter', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    //ANGE
    test('„Active“, „Completed“, „All“ zeigen jeweils die richtigen Todos', async ({ page }: { page: Page }) => {

        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');
        await addTodo(page, 'Dritter Eintrag');


        const checks = page.locator('.todo-list li input[type="checkbox"]');
        await checks.nth(0).check();
        await checks.nth(2).check();

        await page.getByRole('link', { name: 'Active' }).click();
        await expect(page.getByText('Erster Eintrag')).toHaveCount(0);
        await expect(page.getByText('Zweiter Eintrag')).toBeVisible();
        await expect(page.getByText('Dritter Eintrag')).toHaveCount(0);

        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(page.getByText('Erster Eintrag')).toBeVisible();
        await expect(page.getByText('Zweiter Eintrag')).toHaveCount(0);
        await expect(page.getByText('Dritter Eintrag')).toBeVisible();

        await page.getByRole('link', { name: 'All' }).click();
        await expect(page.getByText('Erster Eintrag')).toBeVisible();
        await expect(page.getByText('Zweiter Eintrag')).toBeVisible();
        await expect(page.getByText('Dritter Eintrag')).toBeVisible();
    });
    //RNSR
    test('Count ist korrekt', async ({ page }: { page: Page }) => {
        await addTodo(page, 'Erster Eintrag');
        await addTodo(page, 'Zweiter Eintrag');
        await addTodo(page, 'Dritter Eintrag');

        const checks = page.locator('.todo-list li input[type="checkbox"]');
        await checks.nth(0).check();
        await checks.nth(2).check();


        await page.getByRole('link', { name: 'Active' }).click();
        await expect(page.locator('.todo-count')).toHaveText(/1 item left/);

        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(page.locator('.todo-count')).toHaveText(/1 item left/);

        await page.getByRole('link', { name: 'All' }).click();
        await expect(page.locator('.todo-count')).toHaveText(/1 item left/);
    });

});

test.describe('4. Edge Cases', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    //ANGE
    test('Leere Eingabe', async ({ page }: { page: Page }) => {
        const input = page.getByPlaceholder('What needs to be done?');
        await input.fill('');
        await input.press('Enter');
        const todos = page.locator('.todo-list li');
        await expect(todos).toHaveCount(0);
    });
    //RNSR
    test('sehr langer Text', async ({ page }: { page: Page }) => {
        const langerText = 'A'.repeat(1000);
        await addTodo(page, langerText);
        await expect(page.getByText(langerText)).toBeVisible();
    });
    //ANGE
    test('Verhalten ohne Todos', async ({ page }: { page: Page }) => {
        await expect(page.getByRole('button', { name: 'Clear completed' })).toHaveCount(0);
        const todos = page.locator('.todo-list li');
        await expect(todos).toHaveCount(0);
    });
});