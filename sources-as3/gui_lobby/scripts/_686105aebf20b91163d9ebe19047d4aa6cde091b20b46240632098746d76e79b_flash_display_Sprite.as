package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _686105aebf20b91163d9ebe19047d4aa6cde091b20b46240632098746d76e79b_flash_display_Sprite extends Sprite
   {
       
      
      public function _686105aebf20b91163d9ebe19047d4aa6cde091b20b46240632098746d76e79b_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
