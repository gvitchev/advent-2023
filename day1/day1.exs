defmodule Day1 do
  def is_digit?(<<ch::utf8>>) do
    ch >= ?0 and ch <= ?9
  end

  def process_line(line) when is_binary(line) do
    line
    |> String.graphemes()
    |> Enum.filter(&is_digit?/1)
    |> (fn digits -> hd(digits) <> List.last(digits) end).()
  end
end

samples = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

# samples

File.stream!("input.txt")
|> Stream.map(&Day1.process_line/1)
|> Enum.map(&String.to_integer/1)
|> Enum.sum()
|> IO.puts()
