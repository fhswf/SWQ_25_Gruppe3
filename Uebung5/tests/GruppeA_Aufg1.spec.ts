// Autor: DLWG

import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/#/';
const TODO_INPUT_SELECTOR = '.new-todo';

async function addTodo(page: Page, text: string) {
  await page.locator(TODO_INPUT_SELECTOR).fill(text);
  await page.keyboard.press('Enter');
}

test.describe.serial('ToDo Test - Aufgabe 1', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(TODO_URL);
    // Alle bestehenden Todos löschen
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

  test('Eins & mehrere ToDos hinzufügen', async ({ page }) => {
    await expect(page.locator(TODO_INPUT_SELECTOR)).toBeVisible();
    await addTodo(page, 'Wäsche waschen');
    await expect(page.getByTestId('todo-title')).toBeVisible();
    await expect(page.getByTestId('todo-title')).toContainText('Wäsche waschen');
    await expect(page.getByRole('checkbox', { name: 'Toggle Todo' })).not.toBeChecked();

    await addTodo(page, 'Spülen');
    await expect(page.getByText('Spülen')).toBeVisible();
    const spuelenCheckbox = page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo');
    await expect(spuelenCheckbox).toBeVisible();
    await expect(spuelenCheckbox).not.toBeChecked();
  });

  test('Zweites ToDo ge-toggelt', async ({ page }) => {
    await addTodo(page, 'Wäsche waschen');
    await addTodo(page, 'Spülen');
    const spuelenCheckbox = page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo');
    await spuelenCheckbox.check();
    await expect(spuelenCheckbox).toBeChecked();
  });

  test('"Mark all as complete"', async ({ page }) => {
    await addTodo(page, 'Wäsche waschen');
    await addTodo(page, 'Spülen');
    await page.getByText('Mark all as complete').click();
    const waescheCheckbox = page.getByRole('listitem').filter({ hasText: 'Wäsche waschen' }).getByLabel('Toggle Todo');
    const spuelenCheckbox = page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo');
    await expect(waescheCheckbox).toBeChecked();
    await expect(spuelenCheckbox).toBeChecked();
  });

  test('Prüfe übrige ToDos', async ({ page }) => {
    await addTodo(page, 'Wäsche waschen');
    await addTodo(page, 'Spülen');
    await page.getByText('Mark all as complete').click();
    await expect(page.locator('body')).toContainText('0 items leftAll Active CompletedClear completed');
  });
});
