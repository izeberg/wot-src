package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _13a4bfed537fc379cc77225310408881cff12f7b470e7e93ae5d55a56dc1a8f5_flash_display_Sprite extends Sprite
   {
       
      
      public function _13a4bfed537fc379cc77225310408881cff12f7b470e7e93ae5d55a56dc1a8f5_flash_display_Sprite()
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
