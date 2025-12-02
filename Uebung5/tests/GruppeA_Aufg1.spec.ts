// Autoren: FARN und DLWG

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/#/');
  await expect(page.getByRole('textbox', { name: 'What needs to be done?' })).toBeVisible();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Wäsche waschen');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await expect(page.getByTestId('todo-title')).toBeVisible();
  await expect(page.getByRole('checkbox', { name: 'Toggle Todo' })).toBeVisible();
  await expect(page.getByTestId('todo-title')).toContainText('Wäsche waschen');
  await expect(page.getByRole('checkbox', { name: 'Toggle Todo' })).not.toBeChecked();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Spülen');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await expect(page.getByText('Spülen')).toBeVisible();
  await expect(page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo')).toBeVisible();
  await expect(page.locator('body')).toContainText('Spülen');
  await expect(page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo')).not.toBeChecked();
  await page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo').check();
  await expect(page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo')).toBeChecked();
  await page.getByText('Mark all as complete').click();
  await expect(page.getByRole('listitem').filter({ hasText: 'Wäsche waschen' }).getByLabel('Toggle Todo')).toBeChecked();
  await expect(page.getByRole('listitem').filter({ hasText: 'Spülen' }).getByLabel('Toggle Todo')).toBeChecked();
  await expect(page.locator('body')).toContainText('0 items leftAll Active CompletedClear completed');
  //await expect(page.locator('body')).toContainText('/^0 items.*$/');
});
