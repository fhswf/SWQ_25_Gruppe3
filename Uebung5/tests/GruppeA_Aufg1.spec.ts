// Autoren: FARN und DLWG

import { test, expect, Page } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/#/';
const TODO_INPUT_NAME = 'What needs to be done?';

async function addTodo(page: Page, text: string) {
  const input = page.getByRole('textbox', { name: TODO_INPUT_NAME });
  await input.click();
  await input.fill(text);
  await input.press('Enter');
}

test.describe('TodoMVC', () => {
  test('should add, toggle, and complete todos', async ({ page }) => {
    await page.goto(TODO_URL);

    // Add first todo
    await expect(page.getByRole('textbox', { name: TODO_INPUT_NAME })).toBeVisible();
    await addTodo(page, 'Wäsche waschen');
    await expect(page.getByTestId('todo-title')).toBeVisible();
    await expect(page.getByTestId('todo-title')).toContainText('Wäsche waschen');
    await expect(page.getByRole('checkbox', { name: 'Toggle Todo' })).not.toBeChecked();

    // Add second todo
    await addTodo(page, 'Spülen');
    await expect(page.getByText('Spülen')).toBeVisible();
    const spuelenCheckbox = page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo');
    await expect(spuelenCheckbox).toBeVisible();
    await expect(spuelenCheckbox).not.toBeChecked();

    // Toggle second todo
    await spuelenCheckbox.check();
    await expect(spuelenCheckbox).toBeChecked();

    // Mark all as complete
    await page.getByText('Mark all as complete').click();
    const waescheCheckbox = page.getByRole('listitem').filter({ hasText: 'Wäsche waschen' }).getByLabel('Toggle Todo');
    await expect(waescheCheckbox).toBeChecked();
    await expect(spuelenCheckbox).toBeChecked();

    // Check summary text
    await expect(page.locator('body')).toContainText('0 items leftAll Active CompletedClear completed');
  });
});
