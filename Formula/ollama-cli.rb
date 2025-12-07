class OllamaCli < Formula
  desc "Ollama blob + manifest inspector with orphan detection"
  homepage "https://github.com/r14r/ollama-cli"
  url "https://github.com/r14r/ollama-cli/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "<FILL_ME_IN>"
  license "MIT"

  depends_on "python@3.11"

  def install
    bin.install "ollama-cli.py" => "ollama-cli"
  end

  test do
    output = shell_output("#{bin}/ollama-cli --help")
    assert_match "Inspect Ollama blobs", output
  end
end
