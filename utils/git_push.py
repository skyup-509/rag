from google.colab import userdata
import subprocess

def git_push(commit_message: str):
    # GitHub Token
    github_token = userdata.get("GITHUB_TOKEN")

    if not github_token:
        raise ValueError("GITHUB_TOKEN이 Colab Secret에 없습니다.")

    # 기존 remote URL
    remote_url = subprocess.check_output(
        ["git", "remote", "get-url", "origin"],
        text=True
    ).strip()

    # 인증용 remote 설정
    auth_url = remote_url.replace(
        "https://github.com/",
        f"https://x-access-token:{github_token}@github.com/"
    )

    subprocess.run(
        ["git", "remote", "set-url", "origin", auth_url],
        check=True
    )

    try:
        # Git 사용자 설정
        subprocess.run(
            ["git", "config", "--global", "user.name", "skyup-509"],
            check=True
        )

        subprocess.run(
            ["git", "config", "--global", "user.email", "parkcs0509@gmail.com"],
            check=True
        )

        # 변경사항 추가
        subprocess.run(
            ["git", "add", "-A"],
            check=True
        )

        # 변경사항 확인
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"]
        )

        if result.returncode == 0:
            print("변경사항이 없습니다.")
            return

        # Commit
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True
        )

        # Push
        subprocess.run(
            ["git", "push"],
            check=True
        )

        print(f"✅ Push 완료: {commit_message}")

    finally:
        # Token이 들어간 remote 제거
        subprocess.run(
            ["git", "remote", "set-url", "origin", remote_url],
            check=True
        )
