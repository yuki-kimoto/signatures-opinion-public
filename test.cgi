<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="icon" type="image/x-icon" href="/signatures-opinion-public/images/giblog-logo.png">
<link rel="stylesheet" type="text/css" href="/signatures-opinion-public/css/common.css">

<title>Title - Perl Subroutine Signatures Opinion Blog</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<div class="main">
  <h1>
    <a href="/signatures-opinion-public/">Perl Subroutine Signatures Opinion Blog</a>
  </h1>
  <div>
    This site is an opinion blog about Perl Subroutine Signatures. Subroutine Signatures is plan to added to Perl in the near future. I have a very strong concern in the future of Perl, so I created an independent site about sub signatures. My name is Yuki Kimoto. I'm Perl Light User. I have no media power, community power, political power, and big company power. I just feel and talk about the heart of a weak perl user without a voice.
  </div>
</div>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/signatures-opinion-public/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <!-- bottom -->

  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    Content
  </div>
  <ul>
    <li><a href="/signatures-opinion-public/list.html">Entries</a></li>
    <li><a href="/signatures-opinion-public/blog/20190319121234.html">Why we want subroutine signatures?</a></li>
    <li><a href="/signatures-opinion-public/blog/20191216153849.html">Risk increased by checking the number of subroutine arguments</a><span style="color:gold">★★★</span></li>
    <li><a href="/signatures-opinion-public/blog/20191217163216.html">Are array and hash representations really needed?</a><span style="color:gold">★</span></li>
  </ul>
</div>

        </div>
      </div>
      <div class="footer">
        <!-- footer -->
<a href="https://github.com/yuki-kimoto/giblog">Giblog</a>

      </div>
    </div>
  </body>
</html>
