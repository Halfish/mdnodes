## Material UI

所有的 Component 参考这里：https://mui.com/material-ui/all-components/

- AppBar: 类似 Header；
- Toolbar: 工具栏，放在 AppBar 里面。本身是一个 flex container. 可以用 flex 属性对子控件生效。

## Joy UI

可以替代 Material UI，不一样的设计。

## Base UI

没有 Material UI 的样式，只有最简单的控件，方便自定义。

## MUI System

主要提供一些容器，方便定义一些 css 样式和排版。

### MUI System -> Style utilities

styled

```jsx
import * as React from "react";
import { styled } from "@mui/system";

const MyComponent = styled("div")({
  color: "darkslategray",
  backgroundColor: "aliceblue",
  padding: 8,
  borderRadius: 4,
});

export default function BasicUsage() {
  return <MyComponent>Styled div</MyComponent>;
}
```

### MUI System -> Components

主要包括：`Box / Container / Grid / Stack`

#### Box

Box

- component 属性：默认是一个 div 标签，可以换成其他标签。
- sx 属性：可以用来定义 css 样式，以及访问 theme 里定义的样式。
- system 属性，如 height, width, display 等，都可以直接用。

```jsx
import Box from '@mui/system/Box';

// equivalent to border: '1px solid black'
<Box sx={{ border: 1 }} />

// equivalent to borderColor: theme => theme.palette.primary.main
<Box sx={{ borderColor: 'primary.main' }} />

// equivalent to borderRadius: theme => 2 * theme.shape.borderRadius
<Box sx={{ borderRadius: 2 }} />
// 直接赋值
<Box sx={{ borderRadius: '16px' }} />
```

创建自定义 Box，主要是样式

```jsx
import { createBox, createTheme } from "@mui/system";

const defaultTheme = createTheme({
  // your custom theme values
});

const Box = createBox({ defaultTheme });

export default Box;
```

自定义 component，把 theme 放在外面，就能用 `sx` 属性了。

```jsx
import * as React from "react";
import styled, { ThemeProvider } from "styled-components";
import { unstable_styleFunctionSx } from "@mui/system";
import { createTheme } from "@mui/material/styles";

const theme = createTheme();

const Div = styled("div")(unstable_styleFunctionSx);

export default function StyleFunctionSxDemo() {
  return (
    <ThemeProvider theme={theme}>
      <Div sx={{ m: 1, p: 1, border: 1 }}>Custom component with the sx prop</Div>
    </ThemeProvider>
  );
}
```

#### Container

提供一个能水平居中的容器。

```jsx
<Container maxWidth="sm">

<Container fixed>
```

#### Grid

格子布局

#### Stack

类似与 Flex/Row/Column，水平或者竖直方向的布局。

```jsx
<Stack direction="row" spacing={2}>
  <Item>Item 1</Item>
  <Item>Item 2</Item>
  <Item>Item 3</Item>
</Stack>

<Stack
  direction="row"
  justifyContent="center"
  alignItems="center"
  spacing={2}
>
```

自定义 DatePicker

```js
<LocalizationProvider dateAdapter={AdapterDayjs}>
<DatePicker
  format="YYYY-MM-DD"
  defaultValue={dayjs('2022-04-17')}
  slots={{
    openPickerIcon: DatePickerOpenIcon,
    textField: (textFieldProps) => (
      <TextField
        {...textFieldProps}
        variant="standard"
        size="small"
        InputProps={{ ...textFieldProps['InputProps'], disableUnderline: true }}
        sx={{ width: 120 }}
      />
    ),
  }}
/>
</LocalizationProvider>
```
